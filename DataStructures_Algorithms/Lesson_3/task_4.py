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
    known_host = dict()
    def __init__(self, url):
        self.url = url
        self.hash = (hashlib.pbkdf2_hmac(hash_name='sha512',
                                        password=url.encode(),
                                        salt=url[8:].encode(),
                                        iterations=100000)).hex()
        CashingWebUrl.known_host.update({self.url: self.hash})

def check_known_url(url_to_check: str):
    if url_to_check in CashingWebUrl.known_host:
        return CashingWebUrl[url_to_check]
    else:
        return (hashlib.pbkdf2_hmac(hash_name='sha512',
                                         password=url_to_check.encode(),
                                         salt=url_to_check[8:].encode(),
                                         iterations=100000)).hex()



if __name__ == '__main__':
    yandex = CashingWebUrl('https://yandex.ru')
    yandex_map = CashingWebUrl('https://yandex.ru/maps/')
    print(CashingWebUrl.known_host)
    print(CashingWebUrl.known_host['https://yandex.ru'])
    check_known_url('https://yandex.ru')






