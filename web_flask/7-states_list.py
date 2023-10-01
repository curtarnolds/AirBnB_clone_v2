#!/usr/bin/python3
"""A simple Flask application"""
from flask import Flask, render_template, g
from models import storage


classes = [
        'BaseModel', 'User', 'Place',
        'State', 'City', 'Amenity',
        'Review'
    ]


app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception=None):
    """Remove current SQLAlchemy Session during teardown"""
    storage.close()


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


@app.route('/states_list')
def states_list():
    """Display HTML of list of states"""
    states_obj = storage.all('State')
    states_list = [key for key in states_obj.values()]
    return render_template('7-states_list.html', states=states_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
