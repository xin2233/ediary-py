import sqlite3
from pysqlcipher3 import dbapi2 as sqlite

def create_encrypted_database(password):
    conn = sqlite.connect('diary.db')
    conn.execute("PRAGMA key = '{}'".format(password))
    conn.execute('''
        CREATE TABLE IF NOT EXISTS articles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            author TEXT,
            date TEXT,
            content TEXT
        )
    ''')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS config (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            key TEXT,
            value TEXT
        )
    ''')
    conn.commit()
    conn.close()

# 创建数据库并设置密码
create_encrypted_database('your_password')
