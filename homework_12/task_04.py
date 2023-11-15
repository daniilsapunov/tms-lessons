class WordIterable:
    def __init__(self, txt):
        self.txt = txt.split()
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= len(self.txt):
            raise StopIteration
        current = self.txt[self.count]
        self.count += 1
        return current


if __name__ == '__main__':
    for i in WordIterable('Мама мыла раму'):
        print(i)

    assert ['i', 'like', 'eat'] == [i for i in WordIterable('i like eat')]
    assert ['Возьмите', 'на', 'стажу', 'пожалуйста'] == [i for i in WordIterable('Возьмите на стажу пожалуйста')]
    assert ['i', 'dont', 'like', 'work', 'on', 'factory'] == [i for i in WordIterable('i dont like work on factory')]
    assert ['i', 'likY', 'eat'] != [i for i in WordIterable('i like eat')]