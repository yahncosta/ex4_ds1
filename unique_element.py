from collections import Counter


def find_unique_element(values):
    if not isinstance(values, (list, tuple)):
        raise RuntimeError("Input must be a list or tuple")

    if len(values) % 2 == 0:
        raise RuntimeError("Input length must be odd")

    counts = Counter(values)
    singles = [value for value, count in counts.items() if count == 1]

    if len(singles) != 1:
        raise RuntimeError("Input must contain exactly one element that occurs once")

    if any(count not in (1, 2) for count in counts.values()):
        raise RuntimeError("Elements that are not unique must occur exactly twice")

    return singles[0]