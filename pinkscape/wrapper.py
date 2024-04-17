from io import StringIO
from plum import dispatch
from .et import ET
from .empty import empty_svg_string


class SVG:
    @dispatch
    def __init__(self, figurename: str, filename=None) -> None:
        if filename is not None:
            self.et = ET.parse(filename)
        else:
            self.et = ET.parse(StringIO(empty_svg_string))
        for index in [
            "docname",
            "sodipodi:docname",
            "{http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd}docname",
            "export-filename",
            "inkscape:export-filename",
            "{http://www.inkscape.org/namespaces/inkscape}export-filename",
        ]:
            self.et.getroot().attrib.pop(index, None)
        self.et.getroot().set("sodipodi:docname", f"{figurename}.svg")
        self.et.getroot().set("inkscape:export-filename", f"{figurename}.pdf")

    def __getitem__(self, id):
        try:
            return self.et.findall(f""".//*[@id="{id}"]""")[0]
        except:
            raise Exception(f'Element with id "{id}" not found in tree {self}')

    def add_grid(self, grid):
        self["namedview1"].append(grid)

    def add_layer(self, id, label):
        element = ET.Element(
            "svg:g",
            attrib={
                "inkscape:label": label,
                "inkscape:groupmode": "layer",
                "id": id,
            },
        )
        self.et.getroot().append(element)

    def add_group(self, insert_id, group_id, group_label=None):
        attrib = {
            "id": group_id,
        }
        if group_label is not None:
            attrib["inkscape:label"] = group_label
        element = ET.Element("svg:g", attrib=attrib)
        self[insert_id].append(element)

    def element_remove(self, id):
        parent_map = {c: p for p in self.et.iter() for c in p}
        child = self[id]
        parent = parent_map[child]
        parent.remove(child)

    def element_vacate(self, id):
        parent = self[id]
        for child in list(parent):
            parent.remove(child)

    def write_to(self, filename):
        ET.indent(self.et, space=4 * " ", level=0)
        with open(filename, "wb") as f:
            self.et.write(f, encoding="utf-8", xml_declaration=True)
