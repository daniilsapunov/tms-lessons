"""
# Примечание: Матрица в Python может быть представлена в виде list[list[int]].
# Программа вывести ответ на вопрос (Truе или False), является ли матрица магическим квадратом.
# Магический квадрат - это квадратная матрица, сумма элементов в столбцах, строках и на обеих
# диагоналях (главной и побочной) равны.
#2          2          3
#1 1        1 2        2 7 6
#1 1        2 1        9 5 1
#True       False      4 3 8
#                      True
"""


def create_matrix(size: int) -> list[[]]:
    matrix = []
    for i in range(size):
        rows = []
        for j in input().split():
            rows.append(int(j))
        matrix.append(rows)
    return matrix


def sum_dioganals(matrix: list):

    main_dioganals = 0
    for i in range(len(matrix)):
        main_dioganals += matrix[i][i]

    no_main_diag = 0
    for i in range(len(matrix)):
        no_main_diag += matrix[i][size - i - 1]

    return main_dioganals == no_main_diag == number


def sum_rows(matrix):
    for i in range(len(matrix)):
        sum_r = 0
        for j in range(len(matrix)):
            sum_r += matrix[i][j]
    return sum_r == number


def sum_col(matrix: list[[]]):
    for i in range(len(matrix)):
        sum_column = 0
        for j in range(len(matrix)):
            sum_column += matrix[j][i]
    return sum_column == number


if __name__ == "__main__":
    size = int(input())
    matrix = create_matrix(size)
    number = sum(matrix[0])
    print(matrix)
    print(sum_col(matrix) == sum_rows(matrix) == sum_dioganals(matrix))
