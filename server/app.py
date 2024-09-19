#!/usr/bin/env python3

from flask import Flask, make_response, request, jsonify
from flask_migrate import Migrate

# import model and db instance
from models import db, Sighting

# Initialize Flask app
app = Flask(__name__)

# configure the app
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

# Initialize Flask-Migrate
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

# Initialize the db instance
migrate = Migrate(app, db)
db.init_app(app)


# Define routes and views
@app.route('/')
def index():
    body = {'message': 'The UAPID welcome our new extraterrestrial overlords!'}
    return make_response(body, 200)

@app.route('/sightings')
def get_all_sightings():
    que = Sighting.query.all()
    sightings_list = [p.to_dict() for p in que]
    res = make_response(sightings_list, 200)
    return res 

@app.route('sightings/<int:id>')
def get_sighting_by_id(id):
    sightings_list = [sighting.to_dict() for sighting in Sighting.query.filter_by(id=id)]
    return make_response(sightings_list.to_dict(), 200)

@app.route('/sightings/location/<string:location>')
def get_all_sightings_by_location(location):
    sightings = [sighting.to_dict() for sighting in Sighting.query.filter_by(location=locatoin).all()]
    return make_response(sightings, 200)

@app.route('/sightings/location/<string:location>/date/<string:date>')
def get_all_sightings_by_location_and_date(location, date):
    sightings = [sighting.to_dict() for sighting in Sighting.query.filter_by(location=locatoin, date=date).all()]
    return make_response(sightings, 200)

@app.before_request
def before_request():
    sightings_count = Sighting.query.count()
    print(f'Total sightings: {sightings_count}')

if __name__ == "__main__":
    app.run(port=5555, debug=True)
