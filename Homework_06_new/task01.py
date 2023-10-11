def map_to_tuples(string) -> list:
    return list(map(lambda x: (x.upper(), x.lower()), string.split()))


letters = input()
print(map_to_tuples(letters))

assert map_to_tuples('a B') == [('A', 'a'), ('B', 'b')]
