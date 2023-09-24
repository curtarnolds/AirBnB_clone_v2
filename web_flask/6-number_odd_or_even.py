#!/usr/bin/python3
"""A simple Flask application"""
from flask import Flask, render_template


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
    """Return simple text"""
    return f"C {text.replace('_', ' ')}"


@app.route('/python')
@app.route('/python/')
@app.route('/python/<text>')
def python(text='is cool'):
    """Return simple text"""
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>')
def number(n):
    """Return simple text"""
    return f"{n} is a number"


@app.route('/number_template/<int:n>')
def number_temp(n):
    """Render a template"""
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """Render a template"""
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
