#-*- coding: utf-8 -*-

from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

app.debug = True

client = MongoClient('localhost', 27017)
db = client['searchengine']

@app.route("/")
def index():
    sites = db['sites'].find()
    return render_template('index.html', sites=sites)

@app.route("/newsite", methods=["POST"])
def newsite():
    data = {
        'url': request.form['site']
    }

    if db['sites'].insert(data):
        return redirect('/')

    return redirect('/')

if __name__ == "__main__":
    app.run()