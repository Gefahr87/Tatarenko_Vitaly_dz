/*
 Написать скрипт, отмечающий несовершеннолетних пользователей как неактивных (поле is_active = false).
 Предварительно добавить такое поле в таблицу profiles со значением по умолчанию = true (или 1)
 */
USE vk;

SELECT * FROM profiles
         WHERE FROM_DAYS(DATEDIFF(CURRENT_DATE(), birthday)) < '0018-01-01';