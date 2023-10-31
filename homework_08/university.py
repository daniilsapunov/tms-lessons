from student import Student


students = [Student('Sanya', 6),
            Student('Kirill', 10),
            Student('Serega', 4),
            Student('Dima', 9)]

def cals_sum_scholarship(students: list[Student]):
    return sum([student.get_scholarship() for student in students])

def get_excellent_student_count(students: list[Student]):
    return sum([student.is_excellent() for student in students])



