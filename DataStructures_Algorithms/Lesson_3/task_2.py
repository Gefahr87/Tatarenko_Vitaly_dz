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
from binascii import hexlify

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
                                 " login VARCHAR(255) COMMENT 'Логин пользователя'," \
                                 " password_hash VARCHAR(326) COMMENT 'хэш-пароль пользователя'," \
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

def create_hash(login: str, password: str) -> str:
    hash_obj = hashlib.sha256(password.encode('utf-8'))
    hash_obj_salt = hashlib.pbkdf2_hmac(hash_name='sha256',
                         password=password.encode('utf-8'),
                         salt=login.encode('utf-8'),
                         iterations=100000)
    return hash_obj.hexdigest(), hexlify(hash_obj_salt)

def write_hash_to_mysql(user: str, hash_password):
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
            with connection.cursor() as cursor:
                insert_query = f"INSERT INTO users (login, password_hash) VALUES ({user}, {hash_password});"
                cursor.execute(insert_query)
                connection.commit()
                print("Data write successfully")
        finally:
            connection.close()
    except Exception as ex:
        print("Connection refused...")
        print(ex)


if __name__ == '__main__':
    _, hash = create_hash('user.yser', 'supersuper')
    print('user.yser', hash)
    write_hash_to_mysql(user, str(hash))


