import networkx as nx
import numpy as np
from pprint import pprint
from matplotlib import pyplot as plt
import matplotlib
from math import pi, sqrt
import pinkscape as pink


global_factor = 10
global_offset = 3


def realcolour(a):
    light = 0.5
    return 255 * (light + (1 - light) * a)


def normalise(state, length):
    return length * np.divide(state, np.abs(state))


def operation_ising(re, rng):
    s = re.shape
    re_left_shift = np.roll(re, -1, axis=0)
    re_down_shift = np.roll(re, -1, axis=1)

    prod_to_right = np.multiply(re, re_left_shift)
    prod_to_top = np.multiply(re, re_down_shift)

    edge_to_right = 2 * prod_to_right > rng.exponential(size=s)
    edge_to_top = 2 * prod_to_top > rng.exponential(size=s)

    edges = []
    for i in range(s[0]):
        for j in range(s[1]):
            if edge_to_right[i, j]:
                edges.append(((i, j), (trunc(i + 1), j)))
            if edge_to_top[i, j]:
                edges.append(((i, j), (i, trunc(j + 1))))

    g = nx.Graph()
    g.add_nodes_from(torus.nodes)
    g.add_edges_from(edges)

    component_no = np.zeros(shape=s, dtype=np.int64)
    for k, component in enumerate(nx.connected_components(g)):
        for vertex in component:
            component_no[vertex] = k
    number_of_components = k + 1

    random_bits = rng.integers(low=0, high=2, size=(number_of_components,))
    random_signs = 2 * random_bits - 1

    sign_matrix = np.zeros(shape=s)

    for k in range(number_of_components):
        sign_matrix += random_signs[k] * (component_no == k)

    re_new = np.multiply(re, sign_matrix)

    return re_new


def harmonise_fixed(state):
    a = np.roll(state, -1, axis=0)
    a[-1, :] = 0
    b = np.roll(state, 1, axis=0)
    b[0, :] = 0
    c = np.roll(state, -1, axis=1)
    c[:, -1] = 0
    d = np.roll(state, 1, axis=1)
    d[:, 0] = 0
    return 4 * state + a + b + c + d


def produce_figure(tag, data):
    width, height = data.shape
    angle = (1 / (2 * pi)) * np.remainder(np.imag(np.log(data)), 2 * pi)

    cmap = matplotlib.cm.get_cmap("twilight")

    nstate = normalise(data, 0.5)

    tree = pink.ET.parse("drawings/source/empty.svg")
    layer = tree.findall(""".//*[@id="layer1"]""")[0]

    for k in range(width):
        for j in range(height):
            colour = cmap(angle[k, j])
            print(colour)
            layer.append(
                pink.Circle(
                    pink.cssproperties_from_string(
                        "fill:#{:02x}{:02x}{:02x};stroke:#000000;stroke-width:0.1".format(
                            int(255 * colour[0]),
                            int(255 * colour[1]),
                            int(255 * colour[2]),
                        )
                    ),
                    global_factor * np.array([k + global_offset, j + global_offset]),
                    global_factor / 2,
                ).element()
            )
            layer.append(
                pink.Path(
                    pink.cssproperties_from_string("stroke:#000000;stroke-width:0.5"),
                    global_factor
                    * np.array(
                        [
                            [k + global_offset, j + global_offset],
                            [
                                k + global_offset + np.real(nstate[k, j]),
                                j + global_offset + np.imag(nstate[k, j]),
                            ],
                        ]
                    ),
                ).element()
            )
            # drawer_thin = pt.ShapeStyle()
            # drawer_thin.fill = True
            # drawer_thin.fill_color = f"{{rgb,255:red,{realcolour(colour[0])}; green,{realcolour(colour[1])}; blue,{realcolour(colour[2])}}}"
            # spins.append(drawer_thin(pt.Circle(pt.Vector(k, j), 0.5)))
            # spins.append(drawer(p))
    pink.ET.indent(tree, space=4 * " ", level=0)
    with open(f"drawings/output/{tag}.svg", "wb") as f:
        tree.write(f, encoding="utf-8", xml_declaration=True)
    # fig.draw(spins)
    # fig.write_data()
    # fig.write_standalone()
    # fig.write_include()
    # fig.process()


params = [
    {
        "beta": 0.5,
        "width": 16,
        "height": 16,
        "iterations": 500,
        "ground": False,
        "tag": "sample_T_high",
        "iterations_harm": 0,
        "transpose": False,
        "zoom": None,
        "rng": np.random.default_rng(12345),
    },
    {
        "beta": 3,
        "width": 16,
        "height": 16,
        "iterations": 500,
        "ground": False,
        "tag": "sample_T_low",
        "iterations_harm": 0,
        "transpose": False,
        "zoom": None,
        "rng": np.random.default_rng(151),
    },
    {
        "beta": 0.001,
        "width": 8,
        "height": 8,
        "iterations": 0,
        "ground": False,
        "tag": "vortex",
        "iterations_harm": 2000,
        "transpose": False,
        "zoom": (0, 6, 1, 7),
        "rng": np.random.default_rng(121345),
    },
    {
        "beta": 3,
        "width": 20,
        "height": 20,
        "iterations": 200,
        "ground": False,
        "tag": "spinwave",
        "iterations_harm": 0,
        "transpose": False,
        "zoom": (8, 14, 8, 14),
        "rng": np.random.default_rng(1345),
    },
    {
        "beta": 1,
        "width": 6,
        "height": 6,
        "iterations": 0,
        "ground": True,
        "tag": "ground",
        "iterations_harm": 0,
        "transpose": False,
        "zoom": None,
        "rng": np.random.default_rng(6),
    },
    {
        "beta": 1,
        "width": 32,
        "height": 32,
        "iterations": 4,
        "ground": False,
        "tag": "pair",
        "iterations_harm": 50,
        "transpose": True,
        "zoom": (8, 26, 20, 31),
        "rng": np.random.default_rng(6),
    },
]

for entry in params:
    width = entry["width"]
    height = entry["height"]
    beta = entry["beta"]
    iterations = entry["iterations"]
    tag = entry["tag"]
    iterations_harm = entry["iterations_harm"]
    zoom = entry["zoom"]
    rng = entry["rng"]
    ground = entry["ground"]
    transpose = entry["transpose"]

    if tag != "vortex":
        continue

    assert width == height
    periodic = True
    torus = nx.grid_2d_graph(width, height, periodic)

    def trunc(k):
        return k % width

    assert trunc(-1) == width - 1

    gauss_real = rng.normal(size=(width, height))
    gauss_imaginary = rng.normal(size=(width, height))
    gauss = gauss_real + 1j * gauss_imaginary
    state = sqrt(beta) * np.divide(gauss, np.abs(gauss))

    def operation_cluster(s, rng):
        re, im = np.real(s), np.imag(s)
        return operation_ising(re, rng) + 1j * operation_ising(im, rng)

    def operation_rotate(s, rng):
        rotation = 24 * (1 + 1j) * rng.normal() + 7 * (1 - 1j) * rng.normal()
        rotation = rotation / np.abs(rotation)
        return rotation * s

    for k in range(iterations):
        print(k, iterations)
        state = operation_cluster(state, rng)
        state = operation_rotate(state, rng)

    for k in range(iterations_harm):
        state = normalise(harmonise_fixed(state), 1)

    if ground:
        state = np.ones(shape=(width, height))
        for k in range(1024):
            state = operation_rotate(state, rng)

    if transpose:
        state = state.T

    if zoom is not None:
        state = state[zoom[0] : zoom[1], zoom[2] : zoom[3]]

    produce_figure(tag, state)
