import sqlite3

conn = sqlite3.connect("prodotti.db")


cursor = conn.cursor()


cursor.execute("""CREATE TABLE prodotti
                  (id INTEGER,
                  nome TEXT,
                  prezzo REAL)
               """)

cursor.execute("""CREATE TABLE prodotti_posizione
                  (id INTEGER,
                  pos TEXT)
               """)

prodotti = [
			('1','Mela',0.5),
			('2','Formaggio',2),
			('3','Latte',1),
			('4','Patate',2),
			('5','Bistecca',4.5),
			]

prodotti_posizione=[
			('1','images/cibi/apple.png'),
			('2','images/cibi/cheese.png'),
			('3','images/cibi/milk.png'),
			('4','images/cibi/potatoes.png'),
			('5','images/cibi/steak.png')]

cursor.executemany("INSERT INTO prodotti VALUES (?,?,?)", prodotti)
cursor.executemany("INSERT INTO prodotti_posizione VALUES (?,?)", prodotti_posizione)

conn.commit()