import numpy as np


def get_a_minor_pentatonic_scale_frequencies():
    c1 = 32.7032
    d1 = 36.7081
    e1 = 41.2034
    g1 = 48.9994
    a1 = 55

    result = list()
    result.append(c1 * 1)
    result.append(d1 * 1)
    result.append(e1 * 1)
    result.append(g1 * 1)
    result.append(a1 * 1)

    result.append(c1 * 2)
    result.append(d1 * 2)
    result.append(e1 * 2)
    result.append(g1 * 2)
    result.append(a1 * 2)

    result.append(c1 * 3)
    result.append(d1 * 3)
    result.append(e1 * 3)
    result.append(g1 * 3)
    result.append(a1 * 3)

    result.append(c1 * 4)
    result.append(d1 * 4)
    result.append(e1 * 4)
    result.append(g1 * 4)
    result.append(a1 * 4)

    result.append(c1 * 5)
    result.append(d1 * 5)
    result.append(e1 * 5)
    result.append(g1 * 5)
    result.append(a1 * 5)

    return np.array(result)

