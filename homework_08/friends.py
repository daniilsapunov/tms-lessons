from person import Person

my_friends = [Person('Dima', 22, 'M'),
              Person('Danya', 19, 'M'),
              Person('Nikol', 17, 'F'),
              Person('Britney', 23, 'F'),
              ]

for i in my_friends:
    i.print_person_info()


def get_oldest_person(friends: list[Person]):
    age = 0
    x = my_friends[0]
    for friend in friends:
        if friend.age > age:
            age = friend.age
            x = friend
    x.print_person_info()


def filter_male_person(friends: list[Person]):
    [i.print_person_info() for i in friends if i.gender == 'M']



