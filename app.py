from flask import Flask, flash, redirect, render_template, request, session, abort

app = Flask(__name__)


prodotti=[[1,'mozzarella',3],[2,'pasta',1],[3,'coca_cola','2']]
carrello=[]

@app.route("/")
def index():
    return render_template('index.html',len=len(prodotti), prodotti=prodotti)

@app.route("/hello/<string:name>/")
def hello(name):
    return render_template('test.html',name=name)

def generate_page_list():
    pages = [{"name": "HOME", "url": "www.mario.com"}, {"name": "MEMBERS", "url": "www.members.com"}]
    return pages

@app.route('/inserisci_prodotti', methods=['POST'])
def inserisci_prodotti():
    for prodotto in prodotti:
        value = request.form.getlist(prodotto[1])
        if value:
            carrello.append(prodotto)
    return render_template('carrello.html',len=len(carrello),carrello=carrello)

@app.route('/elimina_prodotti', methods=['POST'])
def elimina_prodotti():
    for prodotto in prodotti[:]:
        value = request.form.getlist(prodotto[1])
        if value:
            carrello.remove(prodotto)
    return render_template('carrello.html',len=len(carrello),carrello=carrello)


@app.route("/back", methods=['POST'])
def back():
    return index()

@app.route("/carrello", methods=['POST'])
def mostra_carrello():
    return render_template('carrello.html',len=len(carrello),carrello=carrello)



if __name__ == "__main__":
    app.run()
