
s = 'asdf'

def is_palindrom(s):
    if s == s[::-1]:
        return True
    else:
        return False

print(is_palindrom(s))



