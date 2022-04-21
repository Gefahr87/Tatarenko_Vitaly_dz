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
import requests

def currency_rates(currency):
    req_answer = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    sym = ['<', '>', '"', '?', '=', '/', "'"]
    inform_content = str(req_answer.content)
    a = len(inform_content)
    for i in range(a):
        for j in range(len(sym)):
            inform_content = inform_content.replace(sym[j], '  ')
    massive = inform_content.split()
    exchange = dict(Date=massive[massive.index('Date') + 1])
    currency_massiv = massive[massive.index(currency): - 1]
    exchange[currency] = currency_massiv[currency_massiv.index('Value') + 1]
    return(exchange)

if __name__=='__main__':
    currency = 'XDR'
    date, value = currency_rates(currency).values()
    print(f'Для валюты {currency} курс на {date} составляет {value}')


