from .et import ET
from plum import dispatch
import numpy as np
from numbers import Number
from .css import CSSProperties


class Shape:
    @dispatch
    def __init__(self, style: CSSProperties):
        self.style = style


class Path(Shape):
    @dispatch
    def __init__(self, style: CSSProperties, path: np.ndarray):
        Shape.__init__(self, style)
        self.path = path

    @dispatch
    def path_string(self) -> str:
        return f'M {" ".join(f"{a[0]},{a[1]}" for a in self.path)}'

    @dispatch
    def element(self) -> ET.Element:
        return ET.Element(
            "svg:path",
            attrib={
                "style": str(self.style),
                "d": self.path_string(),
            },
        )


class ClosedShape(Shape):
    pass


class ClosedPath(Path, ClosedShape):
    @dispatch
    def path_string(self) -> str:
        return Path.path_string(self) + " Z"


class Circle(ClosedShape):
    @dispatch
    def __init__(self, style: CSSProperties, position: np.ndarray, radius: Number):
        ClosedShape.__init__(self, style)
        self.position = position
        self.radius = radius

    @dispatch
    def element(self) -> ET.Element:
        return ET.Element(
            "svg:circle",
            attrib={
                "style": str(self.style),
                "cx": str(self.position[0]),
                "cy": str(self.position[1]),
                "r": str(self.radius),
            },
        )
