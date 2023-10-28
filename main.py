import sqlite3

conn = sqlite3.connect('dsa.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS tab(name TEXT, age INT, tel INT)''')
cursor.execute('''INSERT INTO tab(name, age, tel) VALUES('Sasha', '38', '375447353312') ''')
cursor.execute('''INSERT INTO tab(name, age, tel) VALUES('Petia', '45', '375443987521') ''')
cursor.execute('''INSERT INTO tab(name, age, tel) VALUES('Vasia', '75', '375449756412') ''')
conn.commit()
conn.close()