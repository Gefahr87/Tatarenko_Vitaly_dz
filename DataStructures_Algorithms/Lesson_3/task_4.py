"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница или нет
есть ли в кэше соответствующая страница или нет

Пример кэша: {'url-адрес': 'хеш url-а'; 'url-адрес': 'хеш url-а'; ...}

Если страница в кэше есть, просто вернуть значение хеша, например, 'хеш url-а'
Если страницы в кэше нет, то вычислить хеш и записать в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования
и одного из алгоритмов, например, sha512
Можете усложнить задачу, реализовав ее через ООП
"""
import hashlib


class CashingWebUrl:
    known_host = set()
    def __init__(self, url):
        self.hash = (hashlib.sha512(url.encode())).hexdigest()
        self.url = url
        CashingWebUrl.known_host.add(self.url)
        CashingWebUrl.known_host[self.url] = self.hash


if __name__ == '__main__':
    yandex = CashingWebUrl('https://yandex.ru')
    yandex_map = CashingWebUrl('https://yandex.ru/maps/')
    print(yandex.hash)
    print(CashingWebUrl.known_host)





