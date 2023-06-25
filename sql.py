import sqlite3
connection = sqlite3.connect("tutorial.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE movie(title, year, score)")
cursor.execute("CREATE TABLE book(title, year, score)")


res = cursor.execute("SELECT * FROM sqlite_master")
data = res.fetchone()


print(data)
cursor.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")