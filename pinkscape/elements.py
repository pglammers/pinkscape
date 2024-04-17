from .et import ET


class Shape:
    def __init__(self, style):
        self.style = style


class Path(Shape):
    def __init__(self, style, path):
        Shape.__init__(self, style)
        self.path = path

    def path_string(self):
        return f'M {" ".join(f"{a[0]},{a[1]}" for a in self.path)}'

    def element(self):
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
    def path_string(self):
        return Path.path_string(self) + " Z"


class Circle(ClosedShape):
    def __init__(self, style, position, radius):
        ClosedShape.__init__(self, style)
        self.position = position
        self.radius = radius

    def element(self):
        return ET.Element(
            "svg:circle",
            attrib={
                "style": str(self.style),
                "cx": str(self.position[0]),
                "cy": str(self.position[1]),
                "r": str(self.radius),
            },
        )
