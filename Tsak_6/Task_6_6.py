'''
Реализовать простую систему хранения данных о суммах продаж булочной. Должно быть два
скрипта с интерфейсом командной строки: для записи данных и для вывода на экран
записанных данных. При записи передавать из командной строки значение суммы продаж.
Для чтения данных реализовать в командной строке следующую логику:
● просто запуск скрипта — выводить все записи;
● запуск скрипта с одним параметром-числом — выводить все записи с номера, равного
этому числу, до конца;
● запуск скрипта с двумя числами — выводить записи, начиная с номера, равного
первому числу, по номер, равный второму числу, включительно.
Подумать, как избежать чтения всего файла при реализации второго и третьего случаев.
Данные хранить в файле bakery.csv в кодировке utf-8. Нумерация записей начинается с 1.
Примеры запуска скриптов:
python add_sale.py 5978,5
python add_sale.py 8914,3
python add_sale.py 7879,1
python add_sale.py 1573,7
python show_sales.py
5978,5
8914,3
7879,1
1573,7
python show_sales.py 3
7879,1
1573,7
python show_sales.py 1 3
5978,5
8914,3
7879,1
'''

import sys


def sales_add(*total):
    with open('sale.txt', 'a', encoding='utf-8') as f:
        for el in total:
            f.writelines([el, '\n'])

def sales_result(*calling):
    with open('sale.txt', 'r', encoding='utf-8') as f:
        if len(calling) == 1:
            i = 1
            start = int(*calling)
            for el in f:
                if i >= start:
                    print(el.strip('\n'))
                i += 1
        elif len(calling) == 2:
            i = 1
            start, end = int(calling[0]), int(calling[1])
            for el in f:
                if i >= start and i <= end:
                    print(el.strip('\n'))
                i += 1
        else:
            for el in f:
                print(el.strip('\n'))


# Формат ввода в командную строку: <Режим работа с базой r - read, w - write> <[вывод записей по
#                                   уловиям задачи] or [сумма продаж]>
if sys.argv[1] == 'r':
    sales_result(*sys.argv[2:])
elif sys.argv[1] == 'w':
    sales_add(*sys.argv[2:])
else:
    print('Ошибка ввода. Введите параметры в формате: '\
          '<Режим работа с базой r - read, w - write> '\
          '<[вывод записей по параметрам: "None", или X, или X X] or [сумма продаж для записи в базу]>', '\n'\
          f'Вы ввели {sys.argv[1:]}')