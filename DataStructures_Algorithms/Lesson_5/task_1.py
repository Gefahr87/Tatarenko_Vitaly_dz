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
from collections import Counter


class Company:
    amount_of_companies = 0
    common_profit = 0

    def __init__(self, name: str, lst_of_profit: list):
        self.name = name
        self.quart_profit = lst_of_profit
        self.year_profit = sum(lst_of_profit)
        Company.amount_of_companies += 1
        Company.common_profit += self.year_profit


if __name__ == '__main__':
    n = 0
    comp = []
    # amount_of_company = int(input('Введите количество предприятий для расчета прибыли: '))
    # for number_company in range(amount_of_company):
    #     name = input('Введите название предприятия: ')
    #     quart_profit = list(map(int, input('через пробел введите прибыль данного предприятия '
    #                          'за каждый квартал(Всего 4 квартала): ').split()))
    #     comp.append(Company(name, quart_profit))
    comp.append(Company('Awesome', [235, 345634, 55, 235]))
    comp.append(Company('Great', [345, 34, 543, 34]))
    comp.append(Company('North', [213405, 15434, 5463, 30264]))
    comp.append(Company('South', [3545, 364, 5843, 340]))
    comp.append(Company('West', [13231, 304, 5453, 3499]))
    countr_obj = Counter({cmp.name: cmp.year_profit for cmp in comp})
    print(countr_obj)
    avg_profit_of_companies = countr_obj.total() / Company.amount_of_companies
    above_avarage = {cmp.name for cmp in comp if cmp.year_profit > avg_profit_of_companies}
    below_avarage = {cmp.name for cmp in comp if cmp.year_profit < avg_profit_of_companies}
    print(f'Средняя годовая прибыль всех предприятий: {avg_profit_of_companies}')
    print(f'Предприятия, с прибылью выше среднего значения: {above_avarage}')
    print(f'Предприятия, с прибылью ниже среднего значения: {below_avarage}')

