/*
 Написать скрипт, удаляющий сообщения «из будущего» (дата больше сегодняшней)
 */
USE vk;
DELETE FROM messages WHERE creates_at > CURRENT_DATE();