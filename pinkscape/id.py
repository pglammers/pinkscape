from plum import dispatch
from xml.etree.ElementTree import Element


class ID:
    def __init__(self, tag=None):
        assert type(tag) is str, "not implemented, random tag"
        self.tag = tag
        self.k = 0

    @dispatch
    def __call__(self, element: Element) -> Element:
        element.set("id", f"{self.tag}{self.k}")
        self.k += 1
        return element
