import xml.etree.ElementTree as ET


INKSCAPE_NS = "http://www.inkscape.org/namespaces/inkscape"
SVG_NS = "http://www.w3.org/2000/svg"
SVG_NAMESPACES = {
    "ns": SVG_NS,
    "svg": SVG_NS,
    "dc": "http://purl.org/dc/elements/1.1/",
    "cc": "http://creativecommons.org/ns#",
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "sodipodi": "http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd",
    "inkscape": INKSCAPE_NS,
}
for k, v in SVG_NAMESPACES.items():
    ET.register_namespace(k, v)
