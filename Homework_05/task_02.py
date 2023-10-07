def generate_natural_cubes(n: int) -> list:
    if n > 1:
        return [i ** 3 for i in range(1, n + 1)]

    else:
        return []


assert generate_natural_cubes(3) == [1, 8, 27]
assert generate_natural_cubes(-6) == []
