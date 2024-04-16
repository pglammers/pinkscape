from .et import ET


GRID_SQUARE = ET.Element(
    "inkscape:grid",
    attrib={
        "type": "xygrid",
        "id": "gridFourth",
        "units": "mm",
        "spacingx": "0.25",
        "spacingy": "0.25",
        "empspacing": "4",
    },
)
GRID_TRIANGULAR = ET.Element(
    "inkscape:grid",
    attrib={
        "type": "axonomgrid",
        "id": "gridFourthTriangular",
        "units": "mm",
        "spacingy": "0.25",
        "empspacing": "4",
    },
)
