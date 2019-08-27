import sqlite3
connection = sqlite3.Connection('jeopardy.db')
print(type(connection))
cursor = connection.cursor()
cursor.execute('SELECT name FROM category LIMIT 10')
results = cursor.fetchall()