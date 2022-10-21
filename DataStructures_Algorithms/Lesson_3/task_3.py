"""
Задание 3.
Определить количество различных (уникальных) подстрок
с использованием хеш-функции
Дана строка S длиной N, состоящая только из строчных латинских букв

Подсказка: вы должны в цикле для каждой подстроки вычислить хеш
Все хеши записываем во множество.
Оно отсечет дубли.

Экономия на размере хранимых данных (для длинных строк) и
скорость доступа вместе с уникальностью элементов,
которые даёт множество, сделают решение коротким и эффективным.

Пример:
рара - 6 уникальных подстрок

рар
ра
ар
ара
р
а
"""

import hashlib
from typing import Set


def create_hash(string: str) -> 'hash_sha256':
    hash_obj = hashlib.sha256(string.encode())
    return hash_obj.hexdigest()


if __name__ == '__main__':
    full_string = input('Введите строку: ')
    multiple_trims = dict()
    for lenght_of_sumbol in range(len(full_string)):
        next_symbol = 1
        while True:
            trims = full_string[lenght_of_sumbol: next_symbol + lenght_of_sumbol]
            hash_to_trims = create_hash(trims)
            multiple_trims.update({trims: hash_to_trims})
            next_symbol += 1
            if next_symbol == len(full_string): break
    print(multiple_trims)
    print(len(multiple_trims))
