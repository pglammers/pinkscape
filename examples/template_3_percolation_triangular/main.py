from pinkscape import *
import numpy as np
from colour import Color
import os


directory = os.path.join("examples", "template_3_percolation_triangular")
figure_name = "percolation_triangular"


# Create a random number generator
rng = np.random.default_rng(12345)
width = 100
height = 100


# We start with setting up the canvas.
#   We specify that one unit equals four millimeters on the grid.
#   The x direction points to the right; the y direction points up.
#   Since the origin is in the top-left corner, we take a negative y-offset.
scale = 0.5
offset = np.array([40, -200, 0])
grid = grid_triangular(scale)
transformer = TransformerTriangular(scale, offset)


# Now we setup the identifiers.
#   An identifier gives a unique identifier to each element on the canvas.
#   While this may not be so important in simple use cases, it is good practice.
#   It allows us to select any element in the ElementTree.
#   We create two identifiers because we have two images.
#   Each identifier provides id's starting with "id-pink-", followed by a
#   counter which increments on each application.
id1 = ID("id-pink-")
id2 = ID("id-pink-")


# We now create an empty figure.
#   We only provide the first keyword, namely the figure title.
#   This creates an empty figure.
#   We start by adding our grid to the figure.
#   We also add a new layer, `simulation`.
def figure_empty(title):
    svg = SVG(title)
    svg.add_grid(grid)
    svg.add_layer("simulation", "Simulation")
    return svg


svg1title = f"{figure_name}_raw"
svg1 = figure_empty(svg1title)
l1 = svg1["simulation"]


# We now load a second figure, from an existing `svg` file.
#   If this figure does not exist, another empty figure is loaded instead.
#   The layer `simulation` is emptied.
#   This means that both `svg1` and `svg2` now have an empty layer `simulation`.
#   We shall add our `svg` elements to the layer `simulation`.
#   Other `svg` elements in `svg2` are preserved.
svg2title = f"{figure_name}_editable"
try:
    svg2 = SVG(svg2title, os.path.join(directory, f"{svg2title}.svg"))
    svg2.element_vacate("simulation")
except:
    svg2 = figure_empty(svg2title)
l2 = svg2["simulation"]


# We now describe a style for the circles that we are going to draw.
#   Observe that the `colour` package is used to specify colors.
style_yellow = CSSProperties(
    {
        "fill": Color("yellow"),
        "fill-opacity": 0.8,
        "stroke": "none",
        "stroke-width": 0.5,
        "stroke-opacity": 0.8,
    }
)
style_blue = CSSProperties(
    {
        "fill": Color("blue"),
        "fill-opacity": 0.8,
        "stroke": "none",
        "stroke-width": 0.5,
        "stroke-opacity": 0.8,
    }
)
styles = [style_yellow, style_blue]


hexagon_path = np.array(
    [
        [1, 0, 0],
        [0, 0, -1],
        [0, 1, 0],
        [-1, 0, 0],
        [0, 0, 1],
        [0, -1, 0],
    ]
)
right = np.array([1, 0, -1])
rightup = np.array([0, 1, -1])


# We are now going to draw a bunch of circles.
# We are going to draw 9 vertical rows of circles, each their own group.
# The groups are indexed by `i`.
for i in range(width):

    # We now create a new group, rooted in the `simulation` layer.
    g1 = svg1.add_group(l1, f"group{i}", f"Group {i}")
    g2 = svg2.add_group(l2, f"group{i}", f"Group {i}")

    # We now create a vertical row of 9 circles, indexed by `j`.
    for j in range(height):

        # The canvas position is calculated with our `transformer`.
        this_hexagon = translate(hexagon_path, np.array(i * right + j * rightup))
        path = transformer(this_hexagon)

        # We now create the circle element.
        #   This element does not yet have an id.
        c = ClosedPath(
            styles[rng.integers(low=0, high=2, size=(1,))[0]],
            path,
        )

        # We now add the circle to the correct group in each tree.
        #   Notice that the identifier is used to assign an `id` to each circle.
        g1.append(id1(c.element()))
        g2.append(id2(c.element()))


# Finally, we write the two figures to their respective locations.
svg1.write_to(os.path.join(directory, f"{svg1title}.svg"))
svg2.write_to(os.path.join(directory, f"{svg2title}.svg"))
