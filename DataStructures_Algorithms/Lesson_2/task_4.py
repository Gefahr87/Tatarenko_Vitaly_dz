"""
Задание 4.	Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов - 3, их сумма - 0.75

Решите через рекурсию. В задании нельзя применять циклы.
Нужно обойтисть без создания массива!
"""


def sum_n_element(amount: int, row, sum_element) -> int:
    if amount == 1:
        return sum_element
    else:
        return sum_n_element(amount - 1, row / -2, sum_element) + row / -2


if __name__ == '__main__':
    n = int(input('Введите количество элементов: '))
    row = 1
    sum_element = 1
    print(f'Количество элементов - {n}, их сумма - {sum_n_element(n, row, sum_element)}')