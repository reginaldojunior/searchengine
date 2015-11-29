#-*- coding: utf-8 -*-

from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
db = client['searchengine']

@app.route("/")
def index():
    sites = db['sites'].find()
    return render_template('index.html', sites=sites)

if __name__ == "__main__":
    app.run()