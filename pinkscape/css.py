from plum import dispatch
from colour import Color


def string(object):
    if type(object) is Color:
        return object.hex_l
    else:
        return str(object)


class CSSProperties:
    def __init__(self, properties=None):
        self.properties = properties if type(properties) is dict else dict()
        self.verify()

    def verify(self):
        for k, v in self.items():
            assert str(k) == str(k).strip(), f'The property "{k}" has whitespace'
            assert string(v) == string(v).strip(), f'The value "{v}" has whitespace'

    def __setitem__(self, key, item):
        self.properties[key] = item
        self.verify()

    def __getitem__(self, key):
        self.properties[key]

    def items(self):
        return self.properties.items()

    @dispatch
    def __str__(self) -> str:
        self.verify()
        return ";".join(f"{k}:{string(v)}" for k, v in self.items())


def cssproperties_from_string(cssproperties_string: str) -> CSSProperties:
    list_of_pairs = cssproperties_string.split(";")
    return CSSProperties(dict(map(lambda s: s.split(":"), list_of_pairs)))
