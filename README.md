# pinkscape
`pinkscape` is a lightweight python package. Its objective is to turn python
simulations into figures that are editable with `inkscape`. The output format is
`svg`. For example, `pinkscape` can export a simulation of the Ising model to
`svg`, and you can then add anotations in `inkscape`. After anotation,
`pinkscape` can overwrite the `svg` layer containing the simulation, while
preserving the anotations that were applied to another layer.

## Dependencies
`pinkscape` depends on the following three packages:
1. `xml.etree.ElementTree` for handling the `xml` tree in the `svg` file,
2. `numpy` for handling the positions of points on the canvas,
3. `colour` (https://github.com/vaab/colour) for handling colors.

It also depends `plum-dispatch` for internal type checking.

## Tutorial 
For now there is no tutorial. We refer to the examples for some simple use cases.

## Task list: 
- [ ] Add basic text support
- [ ] Add definitions and arrow tips
- [ ] Add examples
- [ ] Add tutorial
