def remove_vowels(string) -> list:
    return list(filter(lambda x: x.lower() != 'a' and x.lower() != 'e' and x.lower() != 'i' and x.lower() != 'o'
                                 and x.lower() != 'u' and x.lower() != 'y', string.split()))

letters = input()
print(remove_vowels(letters))
assert remove_vowels('a b e') == ['b']
