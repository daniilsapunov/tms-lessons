import re


def is_float_number(string: str) -> bool:
    return re.fullmatch(r'[-+]?[0-9]*\.?[0-9]+', string) is not None

print(is_float_number('+-12.34'))

if __name__ == '__main__':
    assert is_float_number('1231231.12313123')
    assert is_float_number('+1231.12323')
    assert is_float_number('-1231231.12313123')
    assert not is_float_number('o231231.1123')
    assert not is_float_number('--1231231.12313123')
    assert not is_float_number('1231231&12313123')
    assert not is_float_number('1231231!12313123')
    assert not is_float_number('1231231.123asd3123')


