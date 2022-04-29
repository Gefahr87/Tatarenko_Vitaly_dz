'''
Есть два списка:
tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А' ]
Необходимо реализовать генератор, возвращающий кортежи вида (<tutor>, <klass>), например:
Количество генерируемых кортежей не должно быть больше длины списка tutors. Если в списке klasses меньше элементов, чем в списке tutors, необходимо вывести последние кортежи в виде: (<tutor>, None), например:
('Станислав', None)
Доказать, что вы создали именно генератор. Проверить его работу вплоть до истощения.
Подумать, в каких ситуациях генератор даст эффект.
'''

def name_klass(tutors, klasses):
    if len(tutors) < len(klasses):
        for _ in range(len(klasses) - len(tutors)):
            tutors.append('None')
    if len(tutors) > len(klasses):
        for _ in range(len(tutors) - len(klasses)):
            klasses.append('None')
    yield zip(tutors, klasses)

if __name__ == "__main__":
    tutors = ['Иван', 'Анастасия', 'Петр', 'Сергей', 'Дмитрий', 'Борис', 'Елена']
    klasses = ['9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А']
    zip_result = name_klass(tutors, klasses)
    list_result = list(*zip_result)
    for mapping in list_result:
        print(mapping)
    print(next(zip_result))
