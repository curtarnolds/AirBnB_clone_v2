#!/usr/bin/python3
"""A simple Flask application"""
from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """Return 'Hello HBNB'"""
    return "Hello HBNB"


@app.route('/hbnb')
def hbnb():
    """Return 'HBNB'"""
    return "HBNB"


@app.route('/c/<text>')
def text(text):
    return f"C {text.replace('_', ' ')}"


@app.route('/python')
@app.route('/python/')
@app.route('/python/<text>')
def python(text='is cool'):
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>')
def number(n):
    return f"{n} is a number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
