import datetime


class Person:
    def __init__(self, full_name, age, gender):
        self.full_name = full_name
        self.age = age
        self.gender = gender

    def print_person_info(self):
        print(f'Person: {self.full_name} ({self.gender}), {self.age} years old')

    def get_birth_year(self):
        return 2023 - self.age

    def get_birth_year_with_datetime(self):
        years = datetime.datetime.now().year
        return years - self.age
