"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""
from timeit import timeit

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr

if __name__ == '__main__':
    nums = list(range(200))
    print(f'Результатат {func_1(nums)=},\n'
          f'время на выполнение: ', timeit('func_1(nums)', globals=globals(), number=100000))
    print(f'Результатат {func_2(nums)=},\n'
          f'время на выполнение: ', timeit('func_2(nums)', globals=globals(), number=100000))

'''
Вывод: Для сокращения времени выполнения программы был реализован List Comprehension. При малом объёме 
элементов(20) в массиве nums, выиграш около 5%. По мере увеличения количества элементов (200) это процент так же растёт
и достигает уже 20%. 
'''
