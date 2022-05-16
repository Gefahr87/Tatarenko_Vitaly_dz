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

*(вместо 3) Решить задачу 3 для ситуации, когда объём данных в файлах превышает объём
ОЗУ (разумеется, не нужно реально создавать такие большие файлы, это просто задел на
будущее проекта). Только теперь не нужно создавать словарь с данными. Вместо этого нужно
сохранить объединенные данные в новый файл (users_hobby.txt). Хобби пишем через
двоеточие и пробел после ФИО:
Иванов,Иван,Иванович: скалолазание,охота
Петров,Петр,Петрович: горные лыжи
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

with open('user.csv', 'r', encoding='utf-8') as f:
    person = f.readlines()
    for i in range(len(person)):
        person[i] = person[i].replace('\n', '').replace(',', ' ')

f = open('hobby.csv', 'r', encoding='utf-8')
fp = open('users_hobby.txt', 'w', encoding='utf-8')
hobby = f.readlines()
if len(hobby) < len(person):
        for i in range(len(hobby)):
            hobby[i] = hobby[i].replace('\n', '')
            fp.writelines([person[i], ': ', hobby[i].lower(), '\n'])
        for i in range(len(hobby), len(person)):
            fp.writelines([person[i], ': ', 'None', '\n'])
else:
    for i in range(len(person)):
        hobby[i] = hobby[i].replace('\n', '')
        fp.writelines([person[i], ': ', hobby[i].lower(), '\n'])
    sys.exit(1)
f.close()
fp.close()


# for i in range(len(hobby)):
#     hobby[i] = hobby[i].replace('\n', '')
#     fp.writelines([person[i], ': ', hobby[i].lower(), '\n'])
# for i in range(len(hobby), len(person)):
#     fp.writelines([person[i], ': ', 'None', '\n'])

# with open('hobby_test_small.csv', 'r', encoding='utf-8') as f:
#     hobby = f.readlines()
#     for i in range(len(hobby)):
#         hobby[i] = hobby[i].replace('\n', '')
# with open('users_hobby.txt', 'w', encoding='utf-8') as f:
#     if len(hobby) < len(person):
#         for i in range(len(hobby)):
#             f.writelines([person[i], ': ', hobby[i].lower(), '\n'])
#         for i in range(len(hobby), len(person)):
#             f.writelines([person[i], ': ', 'None', '\n'])
#     else:
#         for i in range(len(person)):
#             f.write(person[i])
#             f.write(': ')
#             f.write(hobby[i].lower())
#             f.write('\n')
#         sys.exit(1)






