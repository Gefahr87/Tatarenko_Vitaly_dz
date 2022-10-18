"""
Задание 2.

Ваша программа должна запрашивать пароль
Для этого пароля вам нужно вычислить хеш, используя алгоритм sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно и вновь вычислить хеш
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921
f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль

Важно: для хранения хеша и соли воспользуйтесь или файлом (CSV, JSON)
или, если вы уже знаете, как Python взаимодействует с базами данных,
воспользуйтесь базой данный sqlite, postgres и т.д.
п.с. статья на Хабре - python db-api
"""
import pymysql
from config import host, user, password, db_name
import hashlib

'''
##################### - Инициализация БД и создание таблицы users - #####################
try:
    connection = pymysql.connect(
        host=host,
        port=3306,
        user=user,
        password=password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor
    )
    print("successfully connected...")
    print("#" * 20)

    try:
        cursor = connection.cursor()

        # create DATABASE
        with connection.cursor() as cursor:
            create_database_query = "CREATE DATABASE IF NOT EXISTS Algorithms;"
            cursor.execute(create_database_query)
            print("DATABASE created successfully")

        # create TABLE
        with connection.cursor() as cursor:
            cursor.execute("DROP TABLE IF EXISTS users;")
            create_table_query = "CREATE TABLE users (" \
                                 " id SERIAL PRIMARY KEY," \
                                 " login VARCHAR(255) UNIQUE COMMENT 'Логин пользователя'," \
                                 " password_hash VARCHAR(128) COMMENT 'хэш-пароль пользователя'," \
                                 " created_at DATETIME DEFAULT CURRENT_TIMESTAMP," \
                                 " updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP" \
                                 ") COMMENT 'Пользователи для авторизации';"
            cursor.execute(create_table_query)
            print("Table users created successfully")

    finally:
        connection.close()

except Exception as ex:
    print("Connection refused...")
    print(ex)
#########################################################################################
'''


def init_mysql(func):
    '''Подключение к БД'''
    def _wraper(*args):
        global connection
        try:
            connection = pymysql.connect(
                host=host,
                port=3306,
                user=user,
                password=password,
                database=db_name,
                cursorclass=pymysql.cursors.DictCursor
            )
            print("successfully connected to database...")
            print("#" * 20)

            result = func(*args)

        except Exception as ex:
            print("Connection to database refused...")
            print(ex)
        return result
    return _wraper


def create_hash(login: str, password: str) -> 'hash_sha256 & salt_hash_sha256':
    '''Создание двух видов хэшей: без соли и с ней'''
    hash_obj = hashlib.sha256(login.encode() + password.encode())
    hash_obj_salt = hashlib.pbkdf2_hmac(hash_name='sha256',
                                        password=password.encode(),
                                        salt=login.encode(),
                                        iterations=100000)
    return hash_obj.hexdigest(), hash_obj_salt.hex()


@init_mysql
def write_hash_to_mysql(user_to_write: str, hash_password: str):
    try:
        with connection.cursor() as cursor:
            insert_query = f"""INSERT INTO users (login, password_hash)
             VALUES ('{user_to_write}', '{hash_password}');"""
            cursor.execute(insert_query)
            connection.commit()
            print("Data write in database successfully")
    except pymysql.IntegrityError:  # если пользователь уже есть в базе, то обновляем пароль
        print('Duplicate user in database, starting upgrade data')
        try:
            with connection.cursor() as cursor:
                insert_query = f"""UPDATE users SET password_hash = '{hash_password}'
                 WHERE login = '{user_to_write}';"""
                cursor.execute(insert_query)
                connection.commit()
                print("Data update in database successfully")
        except Exception as ex:
            print("Connection to database refused...")
            print(ex)
    except Exception as ex:
        print("Connection to database refused...")
        print(ex)
    finally:
        connection.close()


@init_mysql
def read_hash_from_mysql(user_to_search: str):
    try:
        with connection.cursor() as cursor:
            insert_query = f"SELECT password_hash FROM users WHERE login = '{user_to_search}';"
            cursor.execute(insert_query)
            row = cursor.fetchall()
            hash_password = row[0]['password_hash']
    finally:
        connection.close()
    return hash_password


def check_to_password(login: str, password_to_check: str):
    if password_to_check == read_hash_from_mysql(login):
        return 'Вы ввели правильный пароль'
    else:
        return 'Вы ввели неверный пароль'


if __name__ == '__main__':
    login, passwrd = 'login1_from_user', input('Введите пароль: ')
    hash, salt_hash = create_hash(login, passwrd)
    print(f'Получен хэш по введённому паролю: {salt_hash}')
    write_hash_to_mysql(login, salt_hash)
    print(check_to_password(login,
                            create_hash(login, input('Введите пароль еще раз для проверки: '))[1]
                            )
          )
