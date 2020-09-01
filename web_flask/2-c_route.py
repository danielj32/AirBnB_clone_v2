#!/usr/bin/python3
""" listening port 5000 """
from flask import Flask, escape, request
app = Flask(__name__)


@app.route('/')
def hello_framework():
    """ display Hello HBNB! """
    return "Hello HBNB!"


@app.route('/hbnb')
def disp_hbnb():
    """ display /hbnb! """
    return "HBNB"


@app.route('/c/<text>')
def show_text(txt):
    """ display /c/<text> """
    return 'C %s' % txt.replace('_', ' ')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    app.url_map.strict_slashes = False
