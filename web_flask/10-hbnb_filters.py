#!/usr/bin/python3
"""A simple Flask application"""
from flask import Flask, render_template
from models import storage
from os import getenv  # noqa


classes = [
        'BaseModel', 'User', 'Place',
        'State', 'City', 'Amenity',
        'Review'
    ]


app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """Remove current SQLAlchemy Session during teardown"""
    storage.close()


@app.route('/hbnb_filters')
def hbnb_filters():
    """Display an HBNB Clone page"""
    states_obj = storage.all('State')
    amenities_obj = storage.all('Amenity')
    states_list = [key for key in states_obj.values()]
    amenities_list = [key for key in amenities_obj.values()]
    return render_template('10-hbnb_filters.html', states=states_list,
                           amenities=amenities_list)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
