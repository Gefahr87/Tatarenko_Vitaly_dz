'''
Написать скрипт, который выводит статистику для заданной папки в виде словаря, в котором
ключи — верхняя граница размера файла (пусть будет кратна 10), а значения — общее
количество файлов (в том числе и в подпапках), размер которых не превышает этой границы,
но больше предыдущей (начинаем с 0), например:
{
100: 15,
1000: 3,
10000: 7,
100000: 2
}
Тут 15 файлов размером не более 100 байт; 3 файла больше 100 и не больше 1000 байт...
Подсказка: размер файла можно получить из атрибута .st_size объекта os.stat.
'''

import os
size_for_result = (100, 1000, 10000, 100000, 1000000)
lst_of_size = []
dict_of_task_folder = dict.fromkeys(size_for_result, 0)

path = os.path.join(os.getcwd(), 'To task 7_4')
os.chdir(path)

for root, folder, files in os.walk(os.getcwd()):
    if files:
        for file in files:
            print(file.split('.')[-1])
            # print(el, os.stat(os.path.join(root, el)), sep='\n')
            path = os.path.join(root, file)
            lst_of_size.append(os.stat(path).st_size)
            # print('\n')
            for margin in size_for_result:
                if os.stat(path).st_size // margin == 0 and os.stat(path).st_size // (margin / 10) != 0\
                     or os.stat(path).st_size == 0 and margin == 100:
                    dict_of_task_folder[margin] += 1
print(dict_of_task_folder)
# lst_of_size.sort()
# print(lst_of_size)

'''
Решил задать пороговые значения списком, тем самым появляется универсальность в плане выставления границ, даже можно 
лёгким преобразованием завернуть в функцию и передавать ей это список и путь иследуемой дирректории, 
а далее использовать как модуль.
Усложнённую задачу не делал, так как пытаюсь догнать сроки выполнения д/з
'''
