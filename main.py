import sqlite3 as db
from posixpath import curdir

with db.connect('student.db') as conn:
    cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    hobby TEXT NOT NULL,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    birth_year INTEGER NOT NULL,
    homeworks REAL NOT NULL)
''')

cursor.execute('''
    INSERT INTO students (hobby, first_name, last_name, birth_year, homeworks) VALUES
    ('reading', 'Ivan', 'Ivanov', 1999, 85.5),
    ('music', 'Anna', 'Petrova', 2000, 12.0),
    ('sports', 'Sergey', 'Sergeevich', 1998, 9.0),
    ('drawing', 'Elena', 'Krasnova', 1997, 15.0),
    ('gaming', 'Pavel', 'Smirnov', 2001, 60.0),
    ('dancing', 'Maria', 'Kuznetsova', 1996, 5.0),
    ('travelling', 'Alex', 'Alexandrov', 2002, 25.0),
    ('fishing', 'Dmitry', 'Dmitriev', 1995, 8.0),
    ('photography', 'Oleg', 'Romanovskiy', 2000, 50.0),
    ('hiking', 'Natalia', 'Sokolova', 1999, 18.0)
    ''')

cursor.execute('''
SELECT * FROM students WHERE LENGTH(last_name) > 10
''')
selected_students = cursor.fetchall()
print(f"Студенты с фамилией длиннее 10 символов: {selected_students}")

cursor.execute('''
UPDATE students
SET first_name = 'genius'
WHERE homeworks > 10
''')


cursor.execute('''
SELECT * FROM students WHERE first_name = 'genius'
''')
geniuses = cursor.fetchall()
print(f"Студенты - гении: {geniuses}")

cursor.execute('''
DELETE FROM students WHERE id % 2 = 0
''')

cursor.execute('''
SELECT * FROM students''')
students = cursor.fetchall()
print(f"Оставшиеся студенты после удаления: {students}")
