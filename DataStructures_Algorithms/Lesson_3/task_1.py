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


def lenght_of_time(func):                                                       # O(1)
    def _wraper(*args):                                                         # O(1)
        start = time.perf_counter()                                             # O(1)
        result = func(*args)                                                    # O(1)
        runtime = time.perf_counter() - start                                   # O(1)
        print(f'Затраченное время на выполнение: {runtime}')                    # O(1)
        return result                                                           # O(1)
    return _wraper                                                              # O(1)


"""a) заполняем словарь и список значениями и замеряем время выполнения"""
@lenght_of_time
def gen_dict_of_random(dct: dict, lenght: int) -> list:                         # O(n)
    for _ in range(lenght):                                                     # O(n)
        value = random()*100                                                    # O(1)
        dct[int(value)] = value                                                 # O(1)
    print('Был сгенерирован словарь.', end=' ')                                 # O(1)
    return dct                                                                  # O(1)


@lenght_of_time
def gen_list_of_random(lst: list, lenght: int) -> list:                         # O(n)
    for _ in range(lenght):                                                     # O(n)
        element = int(random()*100)                                             # O(1)
        lst.append(element)                                                     # O(1)
    print('Был сгенерирован список.', end=' ')                                  # O(1)
    return lst                                                                  # O(1)

'''
Вывод: список заполняется чуть быстрее чем словарь. Словарю нужно доп. время для формирования хэш-таблицы
'''
##########################################################################


"""b) чтение словаря и списка"""
@lenght_of_time
def read_dict(dct: dict, key):                                                  # O(n)
    if key in dct.keys():                                                       # O(n)
        return print(f'По ключу {key=} есть значение {dct[key]}.', end=' ')     # O(1)
    else:
        return print(f'нет {key=}')                                             # O(1)


@lenght_of_time
def read_list(lst: list, number_of_element: int):                               # O(1)
    if len(lst) > number_of_element:                                            # O(1)
        return print(f'На позиции {number_of_element} есть элемент = {lst[number_of_element]}.', end=' ') # O(1)
    else:
        return print(f'нет элемента с порядковым номером {number_of_element}')  # O(1)

'''
Вывод: Чтение списка происзодит быстрее, так как вычисление адреса по известному индексу происходит быстро. 
'''
##########################################################################


"""c) удаление элемента словаря и списка"""
@lenght_of_time
def del_element_dict(dct: dict, key=None):                                      # O(1)
    if key == None:                                                             # O(1)
        dct.popitem()                                                           # O(1)
    else:
        print(f'Удаление ключа {key=}.', end=' ')                               # O(1)
        dct.pop(key)                                                            # O(1)
    print('Было выполнено удаление элемента словаря.', end=' ')                 # O(1)
    return dct                                                                  # O(1)


@lenght_of_time
def del_element_list(lst: list, number_of_element: int):                        # O(1)
    if len(lst) > number_of_element:                                            # O(1)
        lst.pop(number_of_element)                                              # O(1)
    else:
        print(f'нет элемента с порядковым номером {number_of_element}')         # O(1)
    print('Было выполнено удаление элемента cписка.', end=' ')                  # O(1)
    return lst                                                                  # O(1)

'''
Вывод: Удаление элемента словаря происходит немного быстрее, однако извлечение будет дольше в списках по мере
увеличения количества элементов и эта разница будет значительной, это будет связано с использованием хэш-таблиц в 
словаре. 
'''
##########################################################################

if __name__ == '__main__':
    lst = gen_list_of_random([], 100000)
    dct = gen_dict_of_random({}, 100000)
    read_dict(dct, 20)
    read_list(lst, 99)
    del_element_dict(dct, 20)
    del_element_list(lst, 99)
