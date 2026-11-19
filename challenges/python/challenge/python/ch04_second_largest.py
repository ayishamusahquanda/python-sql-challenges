def second_largest_unique(values):
    if not isinstance(values, (list, tuple)):
        raise TypeError("values must be a list or tuple")
    
    largest = None
    second = None

    for v in values:
        if largest is None:
            largest = v
        elif v > largest:
            if second is None or largest > second:
                second = largest
            largest = v
        elif v != largest:
            if second is None or v > second:
                second = v

    return second

tests = [
    [5, 3, 9, 1],
    [10, 8, 12],
    [5, 5, 3],
    [7, 7, 7],
    [5],
    [],
    [-5, -2, -9],
    [2, 2],
    [1, 2, 2, 3],
    [3, 1, 2]
]

for t in tests:
    print(t, "->", second_largest_unique(t))