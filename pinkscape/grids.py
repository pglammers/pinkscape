from .et import ET
import numpy as np
from plum import dispatch


def grid_square(scale=1) -> ET.Element:
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
    def __init__(self, scale, height):
        self.scale = scale
        self.height = height

    def __call__(self, vector: np.ndarray) -> np.ndarray:
        raise NotImplementedError
        return np.ndarray([[-1, 0], [0, 0]]) @ vector


@dispatch
def grid_triangular(scale=1) -> ET.Element:
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
    def __init__(self, scale, height):
        self.scale = scale
        self.height = height

    def __call__(self, vector: np.ndarray) -> np.ndarray:
        raise NotImplementedError
        return np.ndarray([[-1, 0], [0, 0]]) @ vector
