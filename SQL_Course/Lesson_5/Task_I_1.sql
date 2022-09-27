USE shop;
UPDATE users SET created_at = now() WHERE TRUE;
UPDATE users SET updated_at = now() WHERE TRUE;