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


def min_o_linear (lst_obj: list) -> 'dict of index & value min element':    # O(n)
    res = dict.fromkeys(['index_min_el', 'value_min_el'])                   # O(1)
    res['value_min_el'] = lst_obj[0]                                        # O(1)
    for i in range(len(lst_obj)):                                           # n + n + n
        if lst_obj[i] < res['value_min_el']:                                # O(1)
            res['index_min_el'] = i                                         # O(1)
            res['value_min_el'] = lst_obj[i]                                # O(1)
    return res                                                              # O(1)


def min_o_quater (lst_obj: list) -> 'dict of index & value min element':    # O(n^2)
    number_of_rep = len(lst_obj)                                            # n + n
    for _ in range(number_of_rep):                                          # n
        for i in range(number_of_rep-1):                                    # n
            if lst_obj[i] > lst_obj[i+1]:                                   # 1
                lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]         # 1
    return lst_obj                                                          # 1


if __name__ == '__main__':
    print(min_o_linear([9, 5, 7, 8, 3, 4, 10, 1])['value_min_el'])
    print(min_o_quater([9, 5, 7, 8, 3, 4, 10, 1])[0])
