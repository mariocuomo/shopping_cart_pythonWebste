from flask import Flask, flash, redirect, render_template, request, session, abort
from random import randint

app = Flask(__name__)


pages = [{"name": "HOME", "url": "www.mario.com"}, {"name": "MEMBERS", "url": "www.members.com"}]


@app.route("/")
def index():
    return render_template('index.html',pages=pages)

@app.route("/hello/<string:name>/")
def hello(name):
    return render_template('test.html',name=name)

def generate_page_list():
    pages = [{"name": "HOME", "url": "www.mario.com"}, {"name": "MEMBERS", "url": "www.members.com"}]
    return pages


if __name__ == "__main__":
    app.run()