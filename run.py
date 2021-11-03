from flask import Flask, flash, redirect, render_template, request, session, abort
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect("prodotti.db")
cursor = conn.cursor()
cursor.execute("""SELECT * from prodotti""")
prodotti = cursor.fetchall()
prodotti = [list(ele) for ele in prodotti] 


#un prodotto è una lista composta da [id,nome,costo_unitario,quantità, posizione_image]
carrello=[]



@app.route("/")
def index():
    return render_template('index.html')

@app.route("/prodotti")
def home():
    return render_template('home.html',len=len(prodotti), prodotti=prodotti)


@app.route("/hello/<string:name>/")
def hello(name):
    return render_template('test.html',name=name)

def generate_page_list():
    pages = [{"name": "HOME", "url": "www.mario.com"}, {"name": "MEMBERS", "url": "www.members.com"}]
    return pages

@app.route('/inserisci_prodotti', methods=['POST'])
def inserisci_prodotti():
    totale=0
    for prodotto in prodotti:
        value = request.form.getlist(prodotto[1])
        gia_presente = False
        if value:
            for item in carrello:
                if item[1]==prodotto[1]:
                    gia_presente=True;
                    break

            if gia_presente:
                item[4]=item[4]+1;
            else:
                ennupla = prodotto.copy()
                ennupla.append(1)
                carrello.append(ennupla)
            
    for prodotto in carrello:
        totale=totale+(prodotto[4]*prodotto[2])

    return render_template('carrello.html',len=len(carrello),carrello=carrello,totale=totale)

@app.route('/elimina_prodotti', methods=['POST'])
def elimina_prodotti():
    totale=0
    for prodotto in prodotti[:]:
        value = request.form.getlist(prodotto[1])

        if value:
            for item in carrello:
                if item[0]==prodotto[0]:
                    if item[4]>1:
                        item[4]=item[4]-1;
                    else:
                        carrello.remove(item)
        
    for prodotto in carrello:
        totale=totale+(prodotto[4]*prodotto[2])
                        
    return render_template('carrello.html',len=len(carrello),carrello=carrello, totale=totale)


@app.route("/back", methods=['GET'])
def back():
    return home()


@app.route("/carrello", methods=['GET'])
def mostra_carrello():
    totale=0
    for prodotto in carrello:
        totale=totale+(prodotto[4]*prodotto[2])
    return render_template('carrello.html',len=len(carrello),carrello=carrello,totale=totale)



if __name__ == "__main__":
    app.run()
