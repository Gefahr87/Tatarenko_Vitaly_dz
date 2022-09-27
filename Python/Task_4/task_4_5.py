'''
Написать функцию currency_rates(), принимающую в качестве аргумента код валюты
(например, USD, EUR, GBP, ...) и возвращающую курс этой валюты по отношению к рублю.
Использовать библиотеку requests. В качестве API можно использовать
http://www.cbr.ru/scripts/XML_daily.asp. Рекомендация: выполнить предварительно запрос к API
в обычном браузере, посмотреть содержимое ответа. Можно ли, используя только методы класса
str, решить поставленную задачу? Функция должна возвращать результат числового типа,
например float. Подумайте: есть ли смысл для работы с денежными величинами использовать
вместо float тип Decimal? Сильно ли усложняется код функции при этом? Если в качестве
аргумента передали код валюты, которого нет в ответе, вернуть None. Можно ли сделать работу
функции не зависящей от того, в каком регистре был передан аргумент? В качестве примера
выведите курсы доллара и евро.
'''
import datetime

import requests
import datetime as dt
import time

def currency_rates(argv):
    _, *currency = argv
    req_answer = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    sym = ['<', '>', '"', '?', '=', '/', "'"]
    inform_content = str(req_answer.content)
    for i in range(len(sym)):
        inform_content = inform_content.replace(sym[i], '  ')
    massive = inform_content.split()
    exchange = dict(Date = massive[massive.index('Date') + 1])
    for j in range(len(currency)):
        currency_massiv = massive[massive.index(currency[j]): - 1]
        exchange[currency[j]] = currency_massiv[currency_massiv.index('Value') + 1]
    print(exchange)
    date_req, *value = exchange.values()
    dd, mm, year = list(map(int, date_req.split('.')))
    for i in range(len(currency)):
        print(f'Для валюты {currency[i]} курс на {datetime.date(year, mm, dd)} составляет {value[i]}')
    return 0

if __name__=='__main__':
    import sys
    exit(currency_rates(sys.argv))

