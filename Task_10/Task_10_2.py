'''
Реализовать проект расчёта суммарного расхода ткани на производство одежды. Основная
сущность (класс) этого проекта — одежда, которая может иметь определённое название. К
типам одежды в этом проекте относятся пальто и костюм. У этих типов одежды существуют
параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H
соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто
(V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Выполнить общий подсчёт расхода ткани. Проверить на практике полученные на этом уроке
знания. Реализовать абстрактные классы для основных классов проекта и проверить работу
декоратора @property.
'''
from abc import abstractmethod

class Cloths:
    def __init__(self, param_1):
        self.param_1 = param_1

    @property
    @abstractmethod
    def jeket(self):
        return (self.param_1 / 6.5 + 0.5)

    @property
    @abstractmethod
    def costume(self):
        return (2 * self.param_1 + 0.3)

cloth_1 = Cloths(34)
cloth_2 = Cloths(184)
print(f'Расход ткани по пальто с размером {cloth_1.param_1}:', cloth_1.jeket)
print(f'Расход ткани по костюму с ростом {cloth_2.param_1}:', cloth_2.costume)
