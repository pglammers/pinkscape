from pprint import pprint
from pinkscape import (
    ET,
    cssproperties_from_string,
    Circle,
    ClosedPath,
    Path,
    GRID_SQUARE,
    SVG,
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
svg["layer1"].append(c.element())
svg["layer1"].append(p.element())
svg["namedview1"].append(GRID_SQUARE)
svg.write_to("drawings/output/drawing6.svg")
