from pinkscape import *
import numpy as np
import matplotlib
from pprint import pprint
from colour import Color


scale = 4
offset = np.array([10, -20, 0])
grid = grid_triangular(scale)
transformer = TransformerTriangular(scale, offset)
tag = ID("id-pink-")

svg = SVG("percolation_triangular")
svg.add_grid(grid)
svg.add_layer("simulation", "Simulation")
svg.add_group("simulation", "hexagons", "Hexagons")

style_red = cssproperties_from_string(
    "fill:#8abc0b;fill-opacity:1;stroke:#0064ca;stroke-width:0.499999;stroke-opacity:0.699605"
)
style_red["fill"] = Color(rgb=(1, 0, 0)).hex_l
# cmap = matplotlib.colormaps["twilight"]
# pprint(cmap(1))
# pprint(len(cmap(120)))
# for a in cmap(40):
#     print(a)
# for a in cmap(1):
#     pprint(type(a), a)
# style_red["fill"] = "#ffffff"


for i in range(9):
    for j in range(9):
        c = Circle(
            style_red,
            transformer(np.array([i, j, 0])),
            scale / 2,
        )
        svg[f"hexagons"].append(tag(c.element()))

svg.write_to("drawings/output/percolation_triangular.svg")
