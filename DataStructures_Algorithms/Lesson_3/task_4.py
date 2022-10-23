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


def create_hash_sha512(obj: str):
    return hashlib.pbkdf2_hmac(hash_name='sha512',
                        password=obj.encode(),
                        salt=obj[8:].encode(),
                        iterations=100000).hex()


class CashingWebUrl:
    known_host = dict()
    def __init__(self, url):
        self.url = url
        self.hash = create_hash_sha512(url)
        CashingWebUrl.known_host.update({self.url: self.hash})


def check_known_url(url_to_check: str):
    if url_to_check in CashingWebUrl.known_host:
        return CashingWebUrl.known_host[url_to_check]
    else:
        CashingWebUrl.known_host.update({url_to_check: create_hash_sha512(url_to_check)})
        return f'Новый {url_to_check=} был добавлен в список известных адресов.\n' \
               f'Хэш: {CashingWebUrl.known_host[url_to_check]}'


if __name__ == '__main__':
    CashingWebUrl('https://yandex.ru')
    CashingWebUrl('https://yandex.ru/maps/')
    CashingWebUrl('https://www.gismeteo.ru')
    print(check_known_url('https://www.metro.ru'))

