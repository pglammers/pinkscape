from .et import ET
import numpy as np
from plum import dispatch
from numbers import Number


@dispatch
def grid_square(scale: Number = 1) -> ET.Element:
    return ET.Element(
        "inkscape:grid",
        attrib={
            "type": "xygrid",
            "id": "gridSquare",
            "units": "mm",
            "spacingx": str(scale / 4),
            "spacingy": str(scale / 4),
            "empspacing": "4",
        },
    )


class TRANSFORMER_SQUARE:
    @dispatch
    def __init__(self, scale: Number, height: Number):
        self.scale = scale
        self.height = height

    def __call__(self, vector: np.ndarray) -> np.ndarray:
        raise NotImplementedError
        return np.ndarray([[-1, 0], [0, 0]]) @ vector


@dispatch
def grid_triangular(scale: Number = 1) -> ET.Element:
    return ET.Element(
        "inkscape:grid",
        attrib={
            "type": "axonomgrid",
            "id": "gridTriangular",
            "units": "mm",
            "spacingy": str(scale / 4),
            "empspacing": "4",
        },
    )


class TRANSFORMER_TRIANGULAR:
    @dispatch
    def __init__(self, scale: Number, height: Number):
        self.scale = scale
        self.height = height

    @dispatch
    def __call__(self, vector: np.ndarray) -> np.ndarray:
        raise NotImplementedError
        return np.ndarray([[-1, 0], [0, 0]]) @ vector
