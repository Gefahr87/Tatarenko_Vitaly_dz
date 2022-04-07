"""
Реализовать вывод информации о промежутке времени в зависимости от его
продолжительности duration в секундах:
a. до минуты: <s> сек;
b. до часа: <m> мин <s> сек;
c. до суток: <h> час <m> мин <s> сек;
d. * в остальных случаях: <d> дн <h> час <m> мин <s> сек.
"""
#Программа с неоднократным вводом durarion
from os import remove


"""
d = 0
h = 0
m = 0
s = 0
duration = []
for i in range(int(input('Enter amount enters:'))):
    duration.append(int(input('Enter amount seconds:')))
    d = duration[i] // 86400
    h = (duration[i] % 86400) // 3600
    m = ((duration[i] % 86400) % 3600) // 60
    s = ((duration[i] % 86400) % 3600) % 60
    if duration[i] < 60:
        print(int(s), ' сек ')
    elif duration[i] < 3600:
        print(int(m), ' мин ',str(s), ' сек ')
    elif duration[i] < 86400:
        print(int(h), ' час ',str(m), ' мин ',str(s), ' сек ')
    else:
        print(str(d),' дн ',str(h), ' час ',str(m), ' мин ',str(s), ' сек ')
"""

def naive_realisation(duration: int):
    total_time = ''
    d = 0
    h = 0
    m = 0
    s = 0
    d = duration // 86400
    h = (duration % 86400) // 3600
    m = ((duration % 86400) % 3600) // 60
    s = ((duration % 86400) % 3600) % 60
    print("Duration: ", duration)
    if duration < 60:
        total_time = str(s) + "сек"
    elif duration < 3600:
        total_time = str(m) + " мин " + str(s) + " сек"
    elif duration < 86400:
        total_time = str(h) + ' час ' + str(m) + " мин " + str(s) + " сек"
    else:
        total_time = str(d) + ' дн ' + str(h) + ' час ' + str(m) + " мин " + str(s) + " сек"
    return total_time


def one_cycle_realisation(duration):
    total_time = []
    """
    Решение задачи с использования циклов.
    Можно два, но высший пилотаж через 1 цикл.
    Переменная total_time - строковая переменная,
    содержащая в себе промежуток времени в нужно формате
    """
    d, h, m, s = 0, 0 ,0, 0
    duration = []
    for i in range(int(input('Enter amount enters:'))):
        duration.append(int(input('Enter duration:')))
        d = duration[i] // 86400
        h = (duration[i] % 86400) // 3600
        m = ((duration[i] % 86400) % 3600) // 60
        s = ((duration[i] % 86400) % 3600) % 60
        if duration[i] < 60:
            total_time.append(str(s) + " сек")
            #print(int(s), ' сек ')
        elif duration[i] < 3600:
            total_time.append(str(m) + " мин " + str(s) + " сек")
            #print(int(m), ' мин ',str(s), ' сек ')
        elif duration[i] < 86400:
            total_time.append(str(h) + " час " + str(m) + " мин " + str(s) + " сек")
            #print(int(h), ' час ',str(m), ' мин ',str(s), ' сек ')
        else:
            total_time.append(str(d) + " дн " + str(h) + " час " + str(m) + " мин " + str(s) + " сек")
            #print(str(d),' дн ',str(h), ' час ',str(m), ' мин ',str(s), ' сек ')
        print(total_time[i])
    return total_time

if __name__ == '__main__':
    duration = 628
    print(naive_realisation(duration))
    print(one_cycle_realisation(duration))