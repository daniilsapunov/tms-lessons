def generate_squares(*args: int) -> list:
    return [i ** 2 for i in args]


assert generate_squares(1, 2, 3) == [1, 4, 9]
assert generate_squares(0, -2, -3) == [0, 4, 9]
