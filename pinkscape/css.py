class CSSProperties:
    def __init__(self, properties=None):
        self.properties = properties if type(properties) is dict else dict()
        self.verify()

    def verify(self):
        for k, v in self.items():
            assert str(k) == str(k).strip(), f'The property "{k}" has whitespace'
            assert str(v) == str(v).strip(), f'The value "{v}" has whitespace'

    def __setitem__(self, key, item):
        self.properties[key] = item
        self.verify()

    def __getitem__(self, key):
        self.properties[key]

    def items(self):
        return self.properties.items()

    def __str__(self):
        self.verify()
        return ";".join(f"{k}:{v}" for k, v in self.items())


def cssproperties_from_string(cssproperties_string):
    list_of_pairs = cssproperties_string.split(";")
    return CSSProperties(dict(map(lambda s: s.split(":"), list_of_pairs)))
