"""
Задание 3.

Для этой задачи
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

def version_1 (dict_of_company: dict) -> list:                                  # O(n)
    max_val, max_val_key = [], []                                               # O(1)
    i = 0                                                                       # 0(1)
    while i < 3:                                                                # 0(n) n = 3
        max_val.append(max(dict_of_company.values()))                           # O(n) + O(n) + O(1)
        max_val_key.append(max(dict_of_company, key=dict_of_company.get))       # O(n)
        del dict_of_company[max_val_key[-1]]                                    # O(1)
        i += 1                                                                  # O(1)
    return list(zip(max_val, max_val_key))                                      # O(1)

def version_2(dict_of_company: dict) -> dict:                                   # O(n^2)
    sorted_value = sorted(dict_of_company.values(), reverse=True)               # O(n log n)
    sorted_dict_of_3_company = {}                                               # O(1)
    for val in sorted_value[:3]:                                                # O(n^2)
        for key in dict_of_company.keys():                                      # O(n)
            if dict_of_company[key] == val:                                     # O(1)
                sorted_dict_of_3_company[key] = val                             # O(1)
    return sorted_dict_of_3_company                                             # O(1)

if __name__ == '__main__':
    profit_of_company = {'company_1': 1546879, 'company_2': 852316, 'company_3': 55122231, 'company_3': 46546132,
                         'company_4': 46951326, 'company_5': 6461564}
    print(version_2(profit_of_company))
    print(version_1(profit_of_company))
