from io import StringIO
from .et import ET
from .empty import empty_svg_string


class SVG:
    def __init__(self, filename=None):
        if filename is not None:
            self.et = ET.parse(filename)
        else:
            self.et = ET.parse(StringIO(empty_svg_string))

    def __getitem__(self, id):
        try:
            return self.et.findall(f""".//*[@id="{id}"]""")[0]
        except:
            raise Exception(f'Element with id "{id}" not found in tree {self}')

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
        for child in parent:
            parent.remove(child)

    def write_to(self, filename):
        ET.indent(self.et, space=4 * " ", level=0)
        with open(filename, "wb") as f:
            self.et.write(f, encoding="utf-8", xml_declaration=True)
