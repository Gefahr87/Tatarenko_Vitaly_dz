USE vk;

CREATE TABLE IF NOT EXISTS post_access (
    id TINYINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    type_access ENUM('self', 'friend', 'close_friend', 'everyone') NOT NULL
);

CREATE TABLE IF NOT EXISTS post (
    id SERIAL,
    user_id BIGINT UNSIGNED NOT NULL,
    created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    amount_of_like INT UNSIGNED DEFAULT 0,
    amount_of_viewer INT UNSIGNED DEFAULT 0,
    image_id BIGINT UNSIGNED DEFAULT NULL,
    post_access_id TINYINT UNSIGNED NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (image_id) REFERENCES media (id),
    FOREIGN KEY (post_access_id) REFERENCES post_access (id)
);

CREATE TABLE IF NOT EXISTS interest (
    id SERIAL,
    user_id BIGINT UNSIGNED NOT NULL,
    name VARCHAR(100) NOT NULL,
    description VARCHAR(255),
    link VARCHAR(2048),
    image_id BIGINT UNSIGNED DEFAULT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (image_id) REFERENCES media (id)
);