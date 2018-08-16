import sqlite3

conn = sqlite3.connect('test.db')
curs = conn.cursor()

# curs.execute('DROP TABLE if exists users')
# curs.execute('CREATE TABLE users(login VARCHAR(8),userid INTEGER)')

def create_table(conn, name):
    conn.execute('DROP TABLE if exists %s' % name)
    conn.execute('CREATE TABLE %s (login VARCHAR (8),userid INTEGER )' % name)

def insert_table(conn, str, data):
    conn.executemany(str, data)
    conn.commit()

create_table(conn, "users")

str = "INSERT INTO users VALUES(?,?)"
data = [("john", 100), ("jane", 101)]

insert_table(conn, str, data)

# curs.execute('INSERT  INTO users VALUES ("john",1000)')
# curs.execute('INSERT  INTO users VALUES ("jane",1000)')
curs.execute('SELECT * FROM users')

for eachUser in curs.fetchall():
    print(eachUser)
