"""Models for final project."""
import os
from sqlalchemy import (Column,
                        String,
                        Integer,
                        Date,
                        )
from flask_sqlalchemy import SQLAlchemy

database_name = "casting_agency"
database_path = os.environ['DATABASE_URL']
# database_path = "postgres://uxrbcsfivlrkup:28ec020c292dcdf591f1f2cf9aa43b740703d54658cb6ab10151f418805d19f2@ec2-184-73-249-9.compute-1.amazonaws.com:5432/depma9uda2oaj8"
db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''


def setup_db(app, database_path=database_path):
    """Setting up the database and path."""
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


# def db_drop_and_create_all():
#     """Drop and create all."""
#     db.drop_all()
#     db.create_all()
'''
    Actor Model
'''


class Actor(db.Model):
    """Actor Model."""

    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    gender = Column(String)
    age = Column(String)

    def __init__(self, name, gender, age):
        """Init."""
        self.name = name
        self.gender = gender
        self.age = age

    def insert(self):
        """Insert Method (adds a new plant)."""
        db.session.add(self)
        db.session.commit()

    def update(self):
        """Update Method."""
        db.session.commit()

    def delete(self):
        """Delete Method."""
        db.session.delete(self)
        db.session.commit()

    def format(self):
        """Format the objects for the client on the other side."""
        return {
            'id': self.id,
            'name': self.name,
            'gender': self.gender,
            'age': self.age,
        }

'''
    Movie Model
'''


class Movie(db.Model):
    """Movie model."""

    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(Date)

    def __init__(self, title, release_date):
        """Init method."""
        self.title = title,
        self.release_date = release_date

    def insert(self):
        """Insert method."""
        db.session.add(self)
        db.session.commit()

    def update(self):
        """Update Method."""
        db.session.commit()

    def delete(self):
        """Delete Method."""
        db.session.delete(self)
        db.session.commit()

    def format(self):
        """Format Method."""
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date
        }
