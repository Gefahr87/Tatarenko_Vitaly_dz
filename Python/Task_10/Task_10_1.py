"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод
__init__()), который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде
прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
31 22
37 43
51 86
3 5 32
2 4 6
-1 64 -8
3 5 8 3
8 3 7 1
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном
виде.
Далее реализовать перегрузку метода __add__() для сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно. Первый элемент первой
строки первой матрицы складываем с первым элементом первой строки второй матрицы и пр.
"""

class Matrix():
    def __init__(self, list_for_matrix: list): #подсказка. какой тип данных ждём
        self.matrix = list_for_matrix

    def __str__(self):
        for i in range(len(self.matrix)):
            for one_mtrx in self.matrix:
                if len(one_mtrx) > i:
                    if isinstance(one_mtrx[i], list):
                        for el in one_mtrx[i]:
                            print(f'{el:3d}', end='')
                        print(end=f'{" ":2}')
            print()

    def __add__(self):
        sum_of_matrix_el = []
        for one_mtrx in self.matrix:
            for j in range(len(one_mtrx)):
                try:
                    sum_of_matrix_el[j]
                except:
                    sum_of_matrix_el.append([])
                for k in range(len(one_mtrx[j])):
                    try:
                        sum_of_matrix_el[j][k] += one_mtrx[j][k]
                    except:
                        sum_of_matrix_el[j].append(one_mtrx[j][k])
        print('\nСуммированная матрица:')
        for list_of_sum in sum_of_matrix_el:
            for el in list_of_sum:
                print(f'{el:3d}', end=' ')
            print()

list_of_list = [[[31, 22], [37, 43], [51, 86]], [[3, 5, 32], [2, 4, 6], [-1, 64, 8]],
                [[3, 5, 8, 3], [8, 3, 7, 1]]]
cube = Matrix(list_of_list)
cube.__str__()
cube.__add__()
