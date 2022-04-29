'''
Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:
Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]
'''
import time
import sys

src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
start_time = time.time()
result = [el for el in src if src.count(el) == 1]
print(*result, '\nTime = ', time.time() - start_time, 'Size = ', sys.getsizeof(result))

start_time = time.time()
src_unique = set()
tmp = set()
for el in src:
    if el not in tmp:
        src_unique.add(el)
    else:
        src_unique.discard(el)
    tmp.add(el)
print(src_unique, '\nTime = ', time.time() - start_time, 'Size = ', sys.getsizeof(src_unique) + sys.getsizeof(tmp))
