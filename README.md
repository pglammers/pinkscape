# pinkscape
`pinkscape` is a lightweight python package. Its objective is to turn python
simulations into figures that are editable with `inkscape`. The output format is
`svg`. For example, `pinkscape` can export a simulation of the Ising model to
`svg`, and you can then add annotations in `inkscape`. After annotation,
`pinkscape` can overwrite the `svg` layer containing the simulation, while
preserving the annotations that were applied to another layer.

## Dependencies
`pinkscape` depends on the following three packages:
1. `xml.etree.ElementTree` for handling the `xml` tree in the `svg` file,
2. `numpy` for handling the positions of points on the canvas,
3. `colour` (https://github.com/vaab/colour) for handling colors.

It also depends `plum-dispatch` for internal type checking.

## Tutorial 
There is no tutorial for now, and we refer to the `examples` folder instead.
The following examples are well-annotated.
- `examples/template_0_circles`
- `examples/template_1_circles_triangular`

## Task list
- [ ] Add support for basic text
- [ ] Add support for definitions and arrow tips
- [ ] Clean `examples/template_2_vortex`
