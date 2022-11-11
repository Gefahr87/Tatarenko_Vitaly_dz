"""
Задание 2.

Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив,
элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Попытайтесь решить это задание в двух вариантах
1) через collections

defaultdict(list)
int(, 16)
reduce

Counter.update([iterable-or-mapping]) - https://docs-python.ru/standart-library/modul-collections-python/klass-counter-modulja-collections/

2) через ООП

вспомните про перегрузку методов

__mul__
__add__
"""
from collections import defaultdict
from functools import reduce


def sum_mul_hex(hex_1: str, hex_2: str):
    combine_hex = defaultdict(str)
    max_len = max(len(hex_1), len(hex_2))
    for k in max_len:

        combine_hex[k] += int(k, 16)
    sum_hex = reduce(lambda x, y: int(x, 16) + int(y, 16), dict_hex_1)
    return sum_hex



if __name__ == "__main__":
    x_1 = 'A2'
    x_2 = 'C4F'
    lst_x_1 = list(x_1)
    lst_x_2 = list(x_2)
    print(f"{lst_x_1=}, {lst_x_2}")
    print(int(x_1, 16), int(x_2, 16))
    proizved = int(x_1, 16) * int(x_2, 16)
    print(hex(proizved))
    print('Вызываем функцию: ', sum_mul_hex(lst_x_1, lst_x_2))
