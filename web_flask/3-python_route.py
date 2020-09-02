#!/usr/bin/python3
"""
Script that starts a Flask web application.
"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_framework():
    """
    Function to print hello HBNB!
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def disp_hbnb():
    """ display /hbnb! """
    return 'HBNB'


@app.route('/c/<text>')
def c_is_text(text):
    """ display /c/<text> """
    return 'C %s' % text.replace('_', ' ')


@app.route("/python")
@app.route('/python/<text>/')
def py_text(text='is cool'):
    """hbnb"""
    return 'Python %s' % text.replace('_', ' ')


if __name__ == '__main__':
    app.run()
