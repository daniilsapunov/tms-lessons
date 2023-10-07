def get_longest_word(words:str) -> str:
    maximum = ''
    for i in words.split():
        if len(i) > len(maximum):
            maximum = i
    return maximum


assert get_longest_word("i'm trying keep up with everyone") == 'everyone'
assert  get_longest_word("but it doesn't always work out") == "doesn't"
