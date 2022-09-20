import pymysql
from config import host, user, password, db_name

def main():
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
                cursor.execute("DROP TABLE IF EXISTS profiles_test;")
                create_table_query = "CREATE TABLE profiles_test (" \
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
            with connection.cursor() as cursor:
                insert_query = "INSERT INTO `profiles_test` (user_id, gender, birthday, photo_id, city, country) VALUES (45, 'm', '2000-10-11', 7, 'Santa Cruz', 'Mexico');"
                cursor.execute(insert_query)
                connection.commit()
    #
    #         # with connection.cursor() as cursor:
    #         #     insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Victor', '123456', 'victor@gmail.com');"
    #         #     cursor.execute(insert_query)
    #         #     connection.commit()
    #         #
    #         # with connection.cursor() as cursor:
    #         #     insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Oleg', '112233', 'olegan@mail.ru');"
    #         #     cursor.execute(insert_query)
    #         #     connection.commit()
    #
    #         # with connection.cursor() as cursor:
    #         #     insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Oleg', 'kjlsdhfjsd', 'ole2gan@mail.ru');"
    #         #     cursor.execute(insert_query)
    #         #     connection.commit()
    #         #
    #         # with connection.cursor() as cursor:
    #         #     insert_query = "INSERT INTO `users` (name, password, email) VALUES ('Oleg', '889922', 'olegan3@mail.ru');"
    #         #     cursor.execute(insert_query)
    #         #     connection.commit()
    #
    #         # update data
    #         # with connection.cursor() as cursor:
    #         #     update_query = "UPDATE `users` SET password = 'xxxXXX' WHERE name = 'Oleg';"
    #         #     cursor.execute(update_query)
    #         #     connection.commit()
    #
    #         # delete data
    #         # with connection.cursor() as cursor:
    #         #     delete_query = "DELETE FROM `users` WHERE id = 5;"
    #         #     cursor.execute(delete_query)
    #         #     connection.commit()
    #
    #         # drop table
    #         # with connection.cursor() as cursor:
    #         #     drop_table_query = "DROP TABLE `users`;"
    #         #     cursor.execute(drop_table_query)
    #
    #         # select all data from table
    #         with connection.cursor() as cursor:
    #             select_all_rows = "SELECT * FROM `users`"
    #             cursor.execute(select_all_rows)
    #             # cursor.execute("SELECT * FROM `users`")
    #             rows = cursor.fetchall()
    #             for row in rows:
    #                 print(row)
    #             print("#" * 20)
    #
        finally:
            connection.close()

    except Exception as ex:
        print("Connection refused...")
        print(ex)


if __name__ == "__main__":
    main()
