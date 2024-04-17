from pprint import pprint
from pinkscape import (
    ET,
    cssproperties_from_string,
    Circle,
    ClosedPath,
    Path,
    GRID_SQUARE,
    GRID_TRIANGULAR,
    SVG,
    ID,
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


svg = SVG()
tag = ID("id-")
svg["layer1"].append(tag(c.element()))
svg["layer1"].append(tag(p.element()))
svg.add_layer("layer2", "Layer 2")
svg.add_group("layer2", "group1", "Group 1")
svg["group1"].append(tag(p.element()))
svg.element_vacate("group1")
svg["group1"].append(tag(p.element()))
svg.element_remove("layer2")
svg.add_grid(GRID_TRIANGULAR)
svg.write_to("drawings/output/drawing6.svg")
