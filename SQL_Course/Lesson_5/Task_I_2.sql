/*
 Таблица users была неудачно спроектирована.
 Записи created_at и updated_at были заданы типом VARCHAR и в них долгое время помещались значения
 в формате "20.10.2017 8:10". Необходимо преобразовать поля к типу DATETIME, сохранив введеные ранее значения.
 */

USE shop;

ALTER TABLE users MODIFY COLUMN created_at VARCHAR(255);
ALTER TABLE users MODIFY COLUMN updated_at VARCHAR(255);

UPDATE users SET created_at = (case
                                            when id = 1 then '10.12.2017 08:10'
                                            when id = 2 then '15.01.2021 11:11'
                                            when id = 3 then '01.01.2025 01:02'
                                            when id = 4 then '02.01.2021 01:03'
                                            when id = 5 then '03.01.2021 01:04'
                                            when id = 6 then '04.01.2021 01:05'
                                        end),
                         updated_at = (case
                                            when id = 1 then '30.10.2019 10:10'
                                            when id = 2 then '20.05.2022 01:01'
                                            when id = 3 then '13.01.2021 14:14'
                                            when id = 4 then '14.01.2021 15:15'
                                            when id = 5 then '16.01.2021 16:16'
                                            when id = 6 then '17.01.2021 17:17'
                                        end)
                         WHERE id in (1, 2, 3, 4, 5, 6);


DROP TABLE IF EXISTS users_draw;
CREATE TABLE users_draw
(
    id bigint unsigned auto_increment primary key,
    created_at  DATETIME,
    updated_at  DATETIME,
    constraint id
    unique (id)
);

INSERT INTO users_draw(created_at, updated_at)
    SELECT STR_TO_DATE(users.created_at, '%d.%m.%Y %H:%i'),
           STR_TO_DATE(users.updated_at, '%d.%m.%Y %H:%i')
    FROM users;

UPDATE users u1, users_draw u2
    SET u1.created_at = u2.created_at,
        u1.updated_at = u2.updated_at
    WHERE u1.id = u2.id;

ALTER TABLE users MODIFY COLUMN created_at DATETIME;
ALTER TABLE users MODIFY COLUMN updated_at DATETIME;

DROP TABLE IF EXISTS users_draw;

