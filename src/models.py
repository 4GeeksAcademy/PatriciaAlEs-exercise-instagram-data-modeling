import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er



Base = declarative_base()

    # Here we define columns for the table User
    # Notice that each column is also a normal Python instance attribute.
class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    username = Column(String(30), nullable=False, unique=True)
    email = Column(String(30), nullable=False, unique=True)
    firstname = Column(String(30), nullable=False)
    lastname = Column(String(30), nullable=False)
    

class Follower(Base):
    __tablename__ = 'Follower' 
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('User.id'), primary_key=True)
    user_to_id = Column(Integer, ForeignKey('User.id'), primary_key=True)
    user = relationship(User)


class Post(Base):
    __tablename__ = 'Post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'), nullable=False)
    user = relationship(User)
    coments = relationship('Coment', back_populates='post')
    media = relationship('Media', back_populates='post')


class Media(Base):
    __tablename__ = 'Media'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('Post.id'), nullable=False)
    type = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)


class Coment(Base):
    __tablename__ = 'Coment'
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('User.id'), nullable=False)
    comment_text = Column(String(250))
    post_id = Column(Integer, ForeignKey('Post.id'), nullable=False)

    #User es la tabla con la que se relaciona, y le decimos que vamos a coger el id de la Usera

   




    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
