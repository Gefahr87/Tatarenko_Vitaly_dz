import datetime

import requests
import datetime as dt
import time

def currency_rates(currency):
    req_answer = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    sym = ['<', '>', '"', '?', '=', '/', "'"]
    inform_content = str(req_answer.content)
    for i in range(len(sym)):
        inform_content = inform_content.replace(sym[i], '  ')
    massive = inform_content.split()
    exchange = dict(Date = massive[massive.index('Date') + 1])
    currency_massiv = massive[massive.index(currency): - 1]
    exchange[currency] = currency_massiv[currency_massiv.index('Value') + 1]
    return(exchange)

if __name__=='__main__':
    currency = 'USD'
    date_req, value = currency_rates(currency).values()
    dd, mm, year = list(map(int, date_req.split('.')))
    print(f'Для валюты {currency} курс на {datetime.date(year, mm, dd)} составляет {value}')
    print(currency_rates(currency))