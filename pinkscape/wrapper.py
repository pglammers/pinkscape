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
        return self.et.findall(f""".//*[@id="{id}"]""")[0]

    def append_to(self, id, element):
        self[id].append(element)

    def write_to(self, filename):
        ET.indent(self.et, space=4 * " ", level=0)
        with open(filename, "wb") as f:
            self.et.write(f, encoding="utf-8", xml_declaration=True)
