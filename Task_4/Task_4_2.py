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

def currency_rates():
    req_answer = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    sym = ['<', '>', '"', '?', '=', '/', "'"]
    inform_content = str(req_answer.content)
    print(inform_content)
    a = len(inform_content)
    for i in range(a):
        for j in range(len(sym)):
            inform_content = inform_content.replace(sym[j], ' ')
    print(inform_content)
    massive = inform_content.split()
    print(massive)
    exchange = dict(Date=massive)
    # k = 0
    # while k < len(massive):
    #     k +=1
    #     exchange = dict(Date = massive[k])
    #     if k == len(massive) - 1:
    #         break
    return(exchange)

if __name__=='__main__':
    print(currency_rates())


