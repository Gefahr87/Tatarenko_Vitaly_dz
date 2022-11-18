"""
Задание 5. На закрепление навыков работы со стеком

Реализуйте собственный класс-структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стопок.
Создание новой стопки происходит при достижении предыдущим
стеком порогового значения.

После реализации структуры, проверьте ее работу на различных сценариях.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
--реализуйте по аналогии с примером, рассмотренным на уроке
--создание нового стопки можно реализовать добавлением нового пустого массива
в массив стопок (lst = [[], [], [], [],....]).
"""

from RandomWordGenerator import RandomWord


class Storage():

    def __init__(self, number_of_stck: int, number_plate_in_stck: int):
        self.stack = []
        self.number_plate_in_stck = number_plate_in_stck
        for _ in range(number_of_stck):
            self.stack.append([])

    def onemore(self, plat):
        for i in range(len(self.stack)):
            if len(self.stack[i]) < self.number_plate_in_stck:
                self.stack[i].append(plat)
                return
        return print('Все полки заполнены')

    def take(self, stck):
        if stck <= len(self.stack):
            return self.stack[stck-1].pop()
        else:
            return print('Не в том шкафу ищешь!')


if __name__ == '__main__':
    word = RandomWord(max_word_size=5, constant_word_size=False, include_digits=True)
    tableware = Storage(3, 10)
    for _ in range(32):
        tableware.onemore(word.generate())
    print(*tableware.stack, sep='\n')
    print(tableware.take(2))
    print(tableware.take(3))
    print(tableware.take(3))
    print(tableware.take(1))
    print(tableware.take(4))
