import sqlite3

conn = sqlite3.connect("prodotti.db")


cursor = conn.cursor()


cursor.execute("""CREATE TABLE prodotti
                  (id INTEGER,
                  nome TEXT,
                  prezzo REAL)
               """)


prodotti = [
			('1','Mozzarella',2),
			('2','Pasta',1),
			('3','Uova',1.3),
			('4','Latte',2),
			('5','Pane',1.10),
			('6','Cola',1.5),
			('6','Patatine',0.8),
			]

cursor.executemany("INSERT INTO prodotti VALUES (?,?,?)", prodotti)
conn.commit()