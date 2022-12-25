import sqlite3

file_name = 'temp0.db'
db = sqlite3.connect(file_name,check_same_thread=False)
cur = db.cursor()
cur.execute(
    """CREATE TABLE IF NOT EXISTS answers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    q1 INTEGER,
    q2 INTEGER,
    q3 INTEGER,
    q4 INTEGER,
    q5 INTEGER);
    """)

cur.execute(
    """CREATE TABLE IF NOT EXISTS questions (
    id_question INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT
    );
    """)

cur.execute(
    """CREATE TABLE IF NOT EXISTS user ( 
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT,
    age INTEGER,
    gender TEXT,
    education TEXT
     );
     """)
cur.execute(
    """
    INSERT INTO questions (id_question, text) VALUES (1,'капибара');
    """)
cur.execute(
    """
    INSERT INTO questions (id_question, text) VALUES (2,'бабочка');
    """)
cur.execute(
    """
    INSERT INTO questions (id_question, text) VALUES (3,'жизнь');
    """)
cur.execute(
    """
    INSERT INTO questions (id_question, text) VALUES (4,'лингвистика');
    """)
cur.execute(
    """
    INSERT INTO questions (id_question, text) VALUES (5,'каникулы');
    """)
db.commit()