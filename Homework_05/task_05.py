
def get_most_frequent_word(words: str) -> str:
    slovarick = {}
    for i in words.split():
        f = words.split()
        ff = f.count(i)
        slovarick[i] = ff
    return max(slovarick, key=slovarick.get)


assert get_most_frequent_word('a a a a bb bb bb b') == 'a'
assert get_most_frequent_word('I probably google too much, what do you think I') == 'I'
