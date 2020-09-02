#!/usr/bin/python3
"""init Flask web app"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_framework():
    """ display Hello HBNB! """
    return 'Hello HBNB!'


@app.route('/hbnb')
def disp_hbnb():
    """ display /hbnb! """
    return 'HBNB'


@app.route('/c/<text>')
def c_is_text(text):
    """ display /c/<text> """
    return 'C %s' % text.replace('_', ' ')


@app.route('/python')
@app.route('/python/(<text>)')
def Python_is_text(txt="is cool"):
    """ display /python/(<text>) """
    return 'Python %s' % txt.replace('_', ' ')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
