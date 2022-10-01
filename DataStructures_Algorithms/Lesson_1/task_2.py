"""
Задание 2.

Реализуйте два алгоритма.

Оба должны обеспечивать поиск минимального значения для списка.

Сложность первого алгоритма должна быть O(n^2) - квадратичная.

Сложность второго алгоритма должна быть O(n) - линейная.


Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
-- нельзя использовать встроенные функции min() и sort()
-- каждый из двух алгоритмов нужно оформить в виде отдельной ф-ции
-- проставьте сложности каждого выражения в двух ваших алгоритмах
"""

def min_Olinear (lst_obj: list) -> 'dict of index & value min element':
    res = dict.fromkeys(['index_min_el', 'value_min_el', 'sorted_lst'])
    res['value_min_el'] = lst_obj[0]
    for i in range(len(lst_obj) - 1):
        if lst_obj[i] < res['value_min_el']:
            res['index_min_el'] = i
            res['value_min_el'] = lst_obj[i]
    return res.items()


if __name__ == '__main__':
    print(min_Oquadr([9, 5, 7, 8, 3, 1, 10, 4]))
