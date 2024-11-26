import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
    )''')

for i in range(10):
    cursor.execute('''
        INSERT INTO Users(username, email, age, balance) VALUES(?, ?, ?, ?)
    ''', (f'user{i}', f'example{i}@gmail.com', i * 10, 1000))

connection.commit()

cursor.execute('''DELETE FROM Users WHERE ROWID IN (SELECT ROWID FROM Users WHERE (ROWID % 3) = 0)''')

connection.commit()

table = cursor.execute('''SELECT * FROM Users''')

for row in table:
    print(row)

connection.close()
