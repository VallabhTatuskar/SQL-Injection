CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL
);
INSERT INTO users (username) VALUES ('admin'), ('user1');
SELECT * FROM users;
