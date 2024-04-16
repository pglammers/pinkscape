from pprint import pprint
from pinkscape import (
    ET,
    cssproperties_from_string,
    Circle,
    ClosedPath,
    Path,
    GRID_SQUARE,
)


style = cssproperties_from_string(
    "fill:#8abc0b;fill-opacity:0.455224;stroke:#0064ca;stroke-width:0.499999;stroke-opacity:0.699605"
)

pprint(style.properties)

c = Circle(
    style,
    (80, 80),
    20,
)
p = Path(
    style,
    [
        [10, 10],
        [10, 20],
        [30, 30],
    ],
)


tree = ET.parse("drawings/source/empty.svg")


layer = tree.findall(""".//*[@id="layer1"]""")[0]
layer.append(c.element())
layer.append(p.element())

view = tree.findall(""".//*[@id="namedview7"]""")[0]
view.append(GRID_SQUARE)

ET.indent(tree, space=4 * " ", level=0)

with open("drawings/output/drawing6.svg", "wb") as f:
    tree.write(f, encoding="utf-8", xml_declaration=True)
