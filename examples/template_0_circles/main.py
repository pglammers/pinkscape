from pinkscape import *
import numpy as np
import os


directory = os.path.join("examples", "template_0_circles")


# We start with setting up the canvas.
#   We specify that one unit equals four millimeters on the grid.
#   The x direction points to the right; the y direction points up.
#   Since the origin is in the top-left corner, we take a negative y-offset.
scale = 4
offset = np.array([10, -20])
grid = grid_square(scale)
transformer = TransformerSquare(scale, offset)


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


svg1title = "circles_raw"
svg1 = figure_empty(svg1title)


# We now load a second figure, from an existing `svg` file.
#   If this figure does not exist, another empty figure is loaded instead.
#   The layer `simulation` is emptied.
#   This means that both `svg1` and `svg2` now have an empty layer `simulation`.
#   We shall add our `svg` elements to the layer `simulation`.
#   Other `svg` elements in `svg2` are preserved.
svg2title = "circles_editable"
try:
    svg2 = SVG(svg2title, os.path.join(directory, f"{svg2title}.svg"))
    svg2.element_vacate("simulation")
except:
    svg2 = figure_empty(svg2title)


# We now describe a style for the circles that we are going to draw.
circle_style = CSSProperties(
    {
        "fill": "#8abc0b",
        "fill-opacity": "0.455224",
        "stroke": "#0064ca",
        "stroke-width": 0.499999,
        "stroke-opacity": "0.699605",
    }
)


# We are now going to draw a bunch of circles.
# We are going to draw 9 vertical rows of circles, each their own group.
# The groups are indexed by `i`.
for i in range(9):

    # We now create a new group, rooted in the `simulation` layer.
    svg1.add_group("simulation", f"group{i}", f"Group {i}")
    svg2.add_group("simulation", f"group{i}", f"Group {i}")

    # We now create a vertical row of 9 circles, indexed by `j`.
    for j in range(9):

        # The canvas position is calculated with our `transformer`.
        position = transformer(np.array([i, j]))

        # We now create the circle element.
        #   This element does not yet have an id.
        c = Circle(circle_style, position, scale / 2)

        # We now add the circle to the correct group in each tree.
        #   Notice that the identifier is used to assign an `id` to each circle.
        svg1[f"group{i}"].append(id1(c.element()))
        svg2[f"group{i}"].append(id2(c.element()))


# To demonstrate all functionality, we are going to vacate/delete some groups.
#   `group1` is vacated, meaning that all its children are removed.
#   `group2` is removed, meaning that the group itself ceases to exist.
svg1.element_vacate("group1")
svg2.element_vacate("group1")
svg1.element_remove("group2")
svg2.element_remove("group2")


# Finally, we write the two figures to their respective locations.
svg1.write_to(os.path.join(directory, f"{svg1title}.svg"))
svg2.write_to(os.path.join(directory, f"{svg2title}.svg"))
