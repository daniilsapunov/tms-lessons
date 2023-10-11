def remove_vowels(string) -> list:
    return list(filter(lambda x: x != 'a' and x != 'e' and x != 'i' and x != 'o' and x != 'u'
                          and x != 'y', string.split()))

letters = input()
print(remove_vowels(letters))
assert remove_vowels('a b e') == ['b']
