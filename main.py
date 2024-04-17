from pinkscape import (
    SVG,
    ID,
    grid_square,
    TransformerSquare,
    Circle,
    cssproperties_from_string,
)
import numpy as np


scale = 4
offset = np.array([10, -20])
grid = grid_square(scale)
transformer = TransformerSquare(scale, offset)
tag = ID("id-pink-")
tag_editable = ID("id-pink-")


style_yellow = cssproperties_from_string(
    "fill:#8abc0b;fill-opacity:0.455224;stroke:#0064ca;stroke-width:0.499999;stroke-opacity:0.699605"
)

svg = SVG()
svg.add_grid(grid)
svg.add_layer("simulation", "Simulation")

svg_editable = SVG("drawings/output/drawing6_editable.svg")
svg_editable.element_vacate("simulation")

for i in range(9):
    svg.add_group("simulation", f"group{i}", f"Group {i}")
    svg_editable.add_group("simulation", f"group{i}", f"Group {i}")
    for j in range(9):
        c = Circle(
            style_yellow,
            transformer(np.array([i, j])),
            scale / 2,
        )
        svg[f"group{i}"].append(tag(c.element()))
        svg_editable[f"group{i}"].append(tag_editable(c.element()))

svg.element_vacate("group1")
svg_editable.element_vacate("group1")
svg.element_remove("group2")
svg_editable.element_remove("group2")
svg.element_remove("group5")
svg_editable.element_remove("group5")
svg.write_to("drawings/output/drawing6.svg")
svg_editable.write_to("drawings/output/drawing6_editable.svg")
