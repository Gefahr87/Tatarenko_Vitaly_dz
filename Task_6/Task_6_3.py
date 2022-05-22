'''
Есть два файла: в одном хранятся ФИО пользователей сайта, а в другом — данные об их хобби.
Известно, что при хранении данных используется принцип: одна строка — один пользователь,
разделитель между значениями — запятая. Написать код, загружающий данные из обоих файлов
и формирующий из них словарь: ключи — ФИО, значения — данные о хобби. Сохранить словарь
в файл. Проверить сохранённые данные. Если в файле, хранящем данные о хобби, меньше
записей, чем в файле с ФИО, задаём в словаре значение None. Если наоборот — выходим из
скрипта с кодом «1». При решении задачи считать, что объём данных в файлах во много раз
меньше объема ОЗУ.
Фрагмент файла с данными о пользователях (users.csv):
Иванов,Иван,Иванович
Петров,Петр,Петрович
Фрагмент файла с данными о хобби (hobby.csv):
скалолазание,охота
горные лыжи
'''

import random
import sys

#######Скопировал из сети список случайных ФИО и привёл в формат по заданию#######
with open('source_user.csv', 'r', encoding='utf-8') as f:
    data = f.readlines()
with open('user.csv', 'w', encoding='utf-8') as f:
    for el in data:
        f.writelines(el.replace(' ', ','))

#######Создаю список хобби из случайных#######
with open('source_hobby.csv', 'r', encoding='utf-8') as f:
    data = f.readlines()
    for i in range(len(data)):
        data[i] = data[i].replace('\n', ', ')

with open('hobby.csv', 'w+', encoding='utf-8') as f: #подобрать режим открытия файла, нарушение запсии в файл и сбой кодировки
    for el in data:
        a = random.sample(data, random.choice([1, 2, 3]))
        num = len(a)
        a[num - 1] = a[num - 1].strip(', ')
        f.writelines(a)
        f.write('\n')
interest_dict = {}
with open('user.csv', 'r', encoding='utf-8') as f:
    person = f.readlines()
    for i in range(len(person)):
        person[i] = person[i].replace('\n', '').replace(',', ' ')

with open('hobby_test_small.csv', 'r', encoding='utf-8') as f:
    hobby = f.readlines()
    for i in range(len(hobby)):
        hobby[i] = hobby[i].replace('\n', '')
if len(hobby) < len(person):
    for i in range(len(hobby)):
        interest_dict[person[i]] = hobby[i]
    for i in range(len(hobby), len(person)):
        interest_dict[person[i]] = 'None'
    print(*interest_dict.items(), sep='\n')
else:
    for i in range(len(person)):
        interest_dict[person[i]] = hobby[i]
    print(*interest_dict.items(), sep='\n')
    sys.exit(1)






