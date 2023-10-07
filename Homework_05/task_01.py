
def is_year_leap(year: int) -> bool:
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

assert is_year_leap(400) == True
assert is_year_leap(2000) == True
assert is_year_leap(2024) == True
assert is_year_leap(1700) == False
assert is_year_leap(2300) == False

