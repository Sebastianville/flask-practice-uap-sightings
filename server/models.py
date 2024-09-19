from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

# Initialize Flask-SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData()

db = SQLAlchemy(metadata=metadata)

# Define the Sighting model
class Sighting (db.Model, SerializerMixin):
    __tablename__ = 'sightings'

    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    date = db.Column(db.String)
    time = db.Column(db.String)
    location = db.Column(db.String)
    shape_of_craft = db.Column(db.String)
    approximate_size = db.Column(db.Integer)
    approximate_speed = db.Column(db.Integer)
    description = db.Column(db.String)
    reporter = db.Column(db.String)
    reporter_reliable_witness = db.Column(db.Boolean)

    def __repr__(self): 
        return f'<Sighting {self.id}, {self.date}, {self.time}, {self.location},{self.shape_of_craft}, {self.approximate_size}, {self.description}, {self.reporter}, {self.reporter_reliable_witnesse}>'