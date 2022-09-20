import pymysql
from config import host, user, password, db_name
from generate_random_list import image_id, user_id, post_access, gender, list_of_date, city, country
from random import choice

def main():
    bth_day = []
    for el in list_of_date(end=[2030, 12, 13], amount_date=50):
        bth_day.append(str(el))

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
                create_database_query = "CREATE DATABASE IF NOT EXISTS test;"
                cursor.execute(create_database_query)
                print("DATABASE created successfully")

            # create table
            with connection.cursor() as cursor:
                cursor.execute("DROP TABLE IF EXISTS profiles;")
                create_table_query = "CREATE TABLE profiles (" \
                                " user_id BIGINT UNSIGNED PRIMARY KEY," \
                                " gender ENUM('f', 'm', 'x') NOT NULL," \
                                " birthday DATE NOT NULL," \
                                " photo_id BIGINT UNSIGNED," \
                                " city VARCHAR(130)," \
                                " country VARCHAR(130)," \
                                " FOREIGN KEY (user_id) REFERENCES users (id));"
                cursor.execute(create_table_query)
                print("Table profiles_test created successfully")

           # insert data
            for usr_id in user_id:
                with connection.cursor() as cursor:
                    insert_query = f"INSERT INTO `profiles` (user_id, gender, birthday, photo_id, city, country)" \
                                   f" VALUES ({usr_id}, '{choice(gender)}', '{choice(bth_day)}', {choice(image_id)}," \
                                   f" '{choice(city)}', '{choice(country)}');"
                    cursor.execute(insert_query)
                    connection.commit()
            print("Data insert successfully")

        finally:
            connection.close()

    except Exception as ex:
        print("Connection refused...")
        print(ex)


if __name__ == "__main__":
    main()
