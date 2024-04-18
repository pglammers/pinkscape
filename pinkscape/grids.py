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


@dispatch
def translate(object: np.ndarray, translation: np.ndarray) -> np.ndarray:
    assert translation.ndim == 1
    if object.ndim == 1:
        return object + translation
    elif object.ndim == 2:
        return object + np.tile(translation, (object.shape[0], 1))


class Transformer:
    @dispatch
    def __init__(self, scale: Number, offset: np.ndarray):
        self.scale = scale
        self.offset = offset

    def __call__(self, object: np.ndarray) -> np.ndarray:
        object = translate(object, self.offset)
        return self.scale * (object @ self.INTERNAL_MATRIX)


class TransformerSquare(Transformer):
    INTERNAL_MATRIX = np.array([[1, 0], [0, -1]])


class TransformerTriangular(Transformer):
    INTERNAL_MATRIX = np.array(
        [
            [0.86602540378, 0.5],
            [0, -1],
            [-0.86602540378, 0.5],
        ]
    )
