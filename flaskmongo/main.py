from flask import Flask
import os
import socket
import pymongo
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://mongo:27017/')

@app.route("/")
def hello():
    visits = 2
    html = "<h3>Hello {name}!</h3>" \
           "<b>Hostname:</b> {hostname}<br/>" \
           "<b>Visits:</b> {visits}"
    return html.format(name="Blah", hostname=socket.gethostname(), visits=visits)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)