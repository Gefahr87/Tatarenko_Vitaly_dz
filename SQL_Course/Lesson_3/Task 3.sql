DROP DATABASE IF EXISTS vk;
CREATE DATABASE IF NOT EXISTS vk;
USE vk;
SHOW TABLES;

DROP TABLE IF EXISTS users;
CREATE TABLE IF NOT EXISTS users (
    id BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    firstname VARCHAR(150) NOT NULL,
    lastname VARCHAR(150) NOT NULL,
    email VARCHAR(150) NOT NULL UNIQUE,
    phone CHAR(11) NOT NULL UNIQUE,
    password_hash CHAR(65) DEFAULT NULL,
    created_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);

# Заполним таблицу
INSERT users VALUES (1, 'Петя', 'Petukhov', 'pety@gmail.com', '89212223344', NULL, DEFAULT);
INSERT users VALUES (DEFAULT, 'Vasya', 'Vasilkov', 'vasya@mail.ru', '89990001122', DEFAULT, DEFAULT);
SELECT * FROM users;


CREATE TABLE profiles (
    user_id BIGINT UNSIGNED PRIMARY KEY,
    gender ENUM('f', 'm', 'x') NOT NULL,
    birthday DATE NOT NULL,
    photo_id BIGINT UNSIGNED,
    city VARCHAR(130),
    country VARCHAR(130),
    FOREIGN KEY (user_id) REFERENCES users (id)
);

INSERT profiles VALUES (1, 'm', '1997-12-01', NULL, 'Moscow', 'Russia');
INSERT profiles VALUES (2, 'm', '1999-10-21', NULL, 'Moscow', 'Russia');

#INSERT profiles VALUES (42, 'm', '1997-12-01', NULL, 'Moscow', 'Russia');

CREATE TABLE messages (
    #SERIAL = BIGINT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE
    id SERIAL PRIMARY KEY,
    from_user_id BIGINT UNSIGNED NOT NULL,
    to_user_id BIGINT UNSIGNED NOT NULL,
    txt TEXT NOT NULL,
    is_delivered BOOLEAN DEFAULT FALSE,
    creates_at DATETIME NOT NULL DEFAULT NOW(),
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    FOREIGN KEY (from_user_id) REFERENCES users (id),
    FOREIGN KEY (to_user_id) REFERENCES users (id)
);

INSERT messages VALUES (default, 1, 2, 'Привет', DEFAULT, DEFAULT, DEFAULT);
INSERT messages VALUES (default, 1, 2, 'Вася', DEFAULT, DEFAULT, DEFAULT);

INSERT messages VALUES (default, 2, 1, 'Привет', DEFAULT, DEFAULT, DEFAULT);
INSERT messages VALUES (default, 2, 1, 'Петя', DEFAULT, DEFAULT, DEFAULT);
UPDATE messages SET is_delivered = 1 WHERE id = 1;
SELECT * FROM messages;

CREATE TABLE friend_requests (
    from_user_id BIGINT UNSIGNED NOT NULL,
    to_user_id BIGINT UNSIGNED NOT NULL,
    accepted BOOL DEFAULT FALSE,
    PRIMARY KEY (from_user_id, to_user_id),
    CONSTRAINT fk_friends_requests_from_user_id FOREIGN KEY (from_user_id) REFERENCES users (id),
    CONSTRAINT fk_friends_requests_to_user_id FOREIGN KEY (to_user_id) REFERENCES users (id)
);

INSERT friend_requests VALUES (1, 2, DEFAULT);
INSERT friend_requests VALUES (2, 1, DEFAULT);

CREATE TABLE communites (
    id SERIAL PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    description VARCHAR(255),
    admin_id BIGINT UNSIGNED NOT NULL,
    INDEX (name),
    FOREIGN KEY (admin_id) REFERENCES users (id)
);

INSERT communites VALUES (DEFAULT, 'Number 1', 'I am number one', 1);
INSERT communites VALUES (DEFAULT, 'Number 2', 'I am number two', 2);

CREATE TABLE communities_users (
    community_id BIGINT UNSIGNED NOT NULL,
    user_id BIGINT UNSIGNED NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (community_id, user_id),
    FOREIGN KEY (community_id) REFERENCES communites (id),
    FOREIGN KEY (user_id) REFERENCES users (id)
);

INSERT communities_users VALUES (1, 2, DEFAULT);

CREATE TABLE media_types (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);
