import sqlite3

conn = sqlite3.connect("prodotti.db")


cursor = conn.cursor()


cursor.execute("""CREATE TABLE prodotti
                  (id INTEGER,
                  nome TEXT,
                  prezzo REAL,
                  pozione TEXT)
               """)


prodotti = [
			('1','Mela',0.5,'images/cibi/apple.png'),
			('2','Formaggio',2,'images/cibi/cheese.png'),
			('3','Latte',1,'images/cibi/milk.png'),
			('4','Patate',2,'images/cibi/potatoes.png'),
			('5','Bistecca',4.5,'images/cibi/steak.png'),
			]

cursor.executemany("INSERT INTO prodotti VALUES (?,?,?,?)", prodotti)

conn.commit()