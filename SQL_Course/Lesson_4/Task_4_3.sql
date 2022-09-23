/*
 Написать скрипт, отмечающий несовершеннолетних пользователей как неактивных (поле is_active = false).
 Предварительно добавить такое поле в таблицу profiles со значением по умолчанию = true (или 1)
 */
USE vk;
ALTER TABLE profiles ADD COLUMN is_active BOOLEAN DEFAULT TRUE;

UPDATE profiles SET is_active = FALSE WHERE FROM_DAYS(DATEDIFF(CURRENT_DATE(), birthday)) < '0018-01-01'; -- мой вариант до подсказки с вебинара

UPDATE profiles SET is_active = FALSE WHERE TIMESTAMPDIFF(YEAR, birthday, CURRENT_DATE()) < 18;
SELECT TIMESTAMPDIFF(YEAR, '2000-02-24', CURRENT_DATE());