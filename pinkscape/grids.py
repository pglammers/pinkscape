from .et import ET


def grid_square(x=1):
    return ET.Element(
        "inkscape:grid",
        attrib={
            "type": "xygrid",
            "id": "gridSquare",
            "units": "mm",
            "spacingx": str(x / 4),
            "spacingy": str(x / 4),
            "empspacing": "4",
        },
    )


def grid_triangular(x=1):
    return ET.Element(
        "inkscape:grid",
        attrib={
            "type": "axonomgrid",
            "id": "gridTriangular",
            "units": "mm",
            "spacingy": str(x / 4),
            "empspacing": "4",
        },
    )
