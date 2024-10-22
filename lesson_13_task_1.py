import random


def print_result(res, header):
    print(header)
    for j in res:
        print(j)


def main():
    row_matrix = int(input('введите кол-во строк матрицы: '))
    col_matrix = int(input('введите кол-во столбцов матрицы: '))
    matrix1 = [[random.randint(-1000, 1000) for i in range(col_matrix)] for j in range(row_matrix)]
    matrix2 = [[random.randint(-1000, 1000) for i in range(col_matrix)] for j in range(row_matrix)]
    print_result(matrix1, "Матрица 1:")
    print_result(matrix2, "Матрица 2:")
    matrix3 = [list(map(sum, zip(*i))) for i in zip(matrix1, matrix2)]
    print_result(matrix3, "Результат сложения двух матриц:")


if __name__ == '__main__':
    main()
