"""
Задание 1.

Пользователь вводит данные о количестве предприятий,
их наименования и прибыль за 4 квартала
(т.е. 4 отдельных числа) для каждого предприятия.
Программа должна определить среднюю прибыль (за год для всех предприятий)
и вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего

Подсказка:
Для решения задачи обязательно примените коллекцию из модуля collections
Для лучшего освоения материала можете сделать
несколько варианто решения этого задания,
применив несколько коллекций из модуля collections

Пример:
Введите количество предприятий для расчета прибыли: 2
Введите название предприятия: Рога
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 235 345634 55 235

Введите название предприятия: Копыта
через пробел введите прибыль данного предприятия
за каждый квартал(Всего 4 квартала): 345 34 543 34

Средняя годовая прибыль всех предприятий: 173557.5
Предприятия, с прибылью выше среднего значения: Рога
Предприятия, с прибылью ниже среднего значения: Копыта
"""
from collections import Counter, namedtuple

#################################Вариант-1##########################################
class Company:
    common_profit = 0

    def __init__(self, name: str, lst_of_profit: list):
        self.name = name
        self.quart_profit = lst_of_profit
        self.year_profit = sum(lst_of_profit)
        Company.common_profit += self.year_profit


if __name__ == '__main__':
    n = 0
    comp = []
    amount_of_company = int(input('Введите количество предприятий для расчета прибыли: '))
    for number_company in range(amount_of_company):
        name = input('Введите название предприятия: ')
        quart_profit = list(map(int, input('через пробел введите прибыль данного предприятия '
                             'за каждый квартал(Всего 4 квартала): ').split()))
        comp.append(Company(name, quart_profit))
    countr_obj = Counter({cmp.name: cmp.year_profit for cmp in comp})
    avg_profit_of_companies = countr_obj.total() / amount_of_company
    above_avarage = {cmp.name for cmp in comp if cmp.year_profit > avg_profit_of_companies}
    below_avarage = {cmp.name for cmp in comp if cmp.year_profit < avg_profit_of_companies}
    print(f'Средняя годовая прибыль всех предприятий: {avg_profit_of_companies}')
    print(f'Предприятия, с прибылью выше среднего значения: {above_avarage}')
    print(f'Предприятия, с прибылью ниже среднего значения: {below_avarage}')
####################################################################################

#################################Вариант-2##########################################
    comp = []
    common_profit = 0
    amount_of_company = int(input('Введите количество предприятий для расчета прибыли: '))
    PROFIT_STAT = namedtuple('quart_profit', 'name q1 q2 q3 q4 year_profit')
    for number_company in range(amount_of_company):
            name = input('Введите название предприятия: ')
            quart_profit = list(map(int, input('через пробел введите прибыль данного предприятия '
                                 'за каждый квартал(Всего 4 квартала): ').split()))
            year_profit = sum(quart_profit)
            common_profit += year_profit
            comp.append(PROFIT_STAT(name=name,
                                    q1=quart_profit[0], q2=quart_profit[1], q3=quart_profit[2], q4=quart_profit[3],
                                    year_profit=year_profit))
    avg_profit_of_companies = common_profit / amount_of_company
    above_avarage = {cmp.name for cmp in comp if sum(cmp[1:]) > avg_profit_of_companies}
    below_avarage = {cmp.name for cmp in comp if sum(cmp[1:]) < avg_profit_of_companies}
    print(f'Средняя годовая прибыль всех предприятий: {avg_profit_of_companies}')
    print(f'Предприятия, с прибылью выше среднего значения: {above_avarage}')
    print(f'Предприятия, с прибылью ниже среднего значения: {below_avarage}')
