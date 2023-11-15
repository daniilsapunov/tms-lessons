import re


def is_date(string: str) -> bool:
    return re.fullmatch(r'\d{2}-\d{2}-\d{4}', string) is not None


if __name__ == '__main__':
    assert is_date('03-12-2022')
    assert is_date('10-01-2023')
    assert is_date('11-05-1999')
    assert not is_date('0f-12-2022')
    assert not is_date('01-G2-2022')
