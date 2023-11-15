import re


def is_float_number(string: str) -> bool:
    return re.fullmatch(r'\+?\-?\d+\.\d+', string) is not None

if __name__ == '__main__':
    assert is_float_number('1231231.12313123')
    assert is_float_number('+1231231.12313123')
    assert is_float_number('-1231231.12313123')
    assert not is_float_number('o231231.1123')
    assert not is_float_number('--1231231.12313123')
    assert not is_float_number('1231231&12313123')
    assert not is_float_number('1231231!12313123')
    assert not is_float_number('1231231.123asd3123')


