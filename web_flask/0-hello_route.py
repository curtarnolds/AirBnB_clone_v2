#!/usr/bin/python3
"""A simple Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
@app.route('/airbnb-onepage/', strict_slashes=False)
def hello_flask():
    """Display 'Hello HBNB'"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
