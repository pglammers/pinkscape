from io import StringIO
from .et import ET
from .empty import empty_svg_string


class SVG:
    def __init__(self, filename=None):
        if filename is not None:
            self.et = ET.parse(filename)
        else:
            self.et = ET.parse(StringIO(empty_svg_string))
