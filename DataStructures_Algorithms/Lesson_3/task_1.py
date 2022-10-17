"""
Задание 1.

Реализуйте функции:

a) заполнение списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   заполнение словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени

b) получение элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   получение элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени

с) удаление элемента списка, оцените сложность в O-нотации (операции нужно провдить в цикле)
   удаление элемента словаря, оцените сложность в O-нотации (операции нужно провдить в цикле)
   сделайте аналитику, что заполняется быстрее и почему
   сделайте замеры времени


ВНИМАНИЕ: в задании три пункта
НУЖНО выполнить каждый пункт
обязательно отделяя каждый пункт друг от друга

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
вы уже знаете, что такое декоратор и как его реализовать,
обязательно реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к своим функциям!
"""


import time
from random import random

def lenght_of_time(func):
    def _wraper(*args):
        start = time.perf_counter()
        result = func(*args)
        runtime = time.perf_counter() - start
        print(f'Затраченное время на выполнение: {runtime}')
        return result
    return _wraper


@lenght_of_time
def gen_dict_of_random(dct: dict, lenght: int) -> list:
    for _ in range(lenght):
        value = random()*100
        dct[int(value)] = value
    return dct


@lenght_of_time
def gen_list_of_random(lst: list, lenght: int) -> list:
    for _ in range(lenght):
        element = int(random()*100)
        lst.append(element)
    return lst

@lenght_of_time
def read_dict(dct: dict, key):
    if key in dct.keys():
        return print(f'по ключу {key=} есть значение {dct[key]}')
    else:
        return print(f'нет {key=}')


if __name__ == '__main__':
    lst = gen_list_of_random([], 100)
    dct = gen_dict_of_random({}, 100)
    read_dict(dct, 20)

