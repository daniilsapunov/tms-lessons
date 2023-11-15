import re


def generate_words(txt: str):
    for i in re.findall(r'\b\w+\b',txt):
        yield i


if __name__ == '__main__':
    for i in generate_words('мама мыла раму'):
        print(i)

    assert ['dont', 'like', 'not', 'hot'] == [i for i in generate_words('dont, like! not^ hot&')]
    assert ['very', 'like', 'be', 'happy'] == [i for i in generate_words("very, like. be! happy")]
