import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Person(Base):
    __tablename__ = 'person'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(250), unique=True, nullable=False)
    password = Column(Integer, nullable=False)

    # def login():
    #     return {
    #         "username": username, 
    #         "password": password
    #     }

class Favorites(Base): 
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    user_id = Column(Integer, ForeignKey('person.id'))
    user = relationship(Person)

class Character(Base):
    __tablename__ = 'characters'
    name = Column(String(250))
    id = Column(Integer, primary_key=True)
    favorite_id = Column(Integer, ForeignKey('favorites.id'))
    favorite = relationship(Favorites)

class Planet(Base):
    __tablename__ = 'planets'
    name = Column(String(250))
    id = Column(Integer, primary_key=True)
    favorite_id = Column(Integer, ForeignKey('favorites.id'))
    favorite = relationship(Favorites)



## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
