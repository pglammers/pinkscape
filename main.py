from pprint import pprint
from pinkscape import (
    ET,
    cssproperties_from_string,
    Circle,
    ClosedPath,
    Path,
    grid_square,
    grid_triangular,
    TransformerSquare,
    SVG,
    ID,
)
import numpy as np


scale = 4
offset = np.array([10, -20])


grid = grid_square(scale)
transformer = TransformerSquare(scale, offset)
tag = ID("id-pink-")


style_yellow = cssproperties_from_string(
    "fill:#8abc0b;fill-opacity:0.455224;stroke:#0064ca;stroke-width:0.499999;stroke-opacity:0.699605"
)


svg = SVG()
svg.add_grid(grid)
svg.add_layer("simulation", "Simulation")


for i in range(9):
    svg.add_group("simulation", f"group{i}", f"Group {i}")
    for j in range(9):
        c = Circle(
            style_yellow,
            transformer(np.array([i, j])),
            scale / 2,
        )
        svg[f"group{i}"].append(tag(c.element()))


svg.element_vacate("group1")
svg.element_remove("group2")
svg.write_to("drawings/output/drawing6.svg")
