"""
Задание 7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.

Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2

Нужно написать рекурсивную ф-цию только для левой части выражения!
Результат нужно сверить с правой частью.
Правой части выражения в рекурсивной ф-ции быть не должно!

Решите через рекурсию. В задании нельзя применять циклы.
"""


def check_equal_func(natur_number: int, check_func: int, idx=0, sum_el=0) -> 'str':
    if idx > natur_number:
        return f'Результат вычислений {sum_el}, а результат функции {check_func}'
    else:
        return check_equal_func(natur_number, check_func, idx + 1, sum_el + idx)


if __name__ == '__main__':
    natur_number = int(input('Введите натуральное число\n'))
    check_func = int((natur_number*(natur_number + 1)) / 2)
    print(check_equal_func(natur_number, check_func))
