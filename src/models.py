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
    # Relación 1 a N con Post (Un usuario puede tener muchos posts)
    posts = relationship('Post', back_populates='user')
    # Relación 1 a N con Coment (Un usuario puede hacer varios comentarios)
    comments = relationship('Coment', back_populates='author')
    

class Follower(Base):
    __tablename__ = 'Follower' 
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('User.id'), nullable=False)
    user_to_id = Column(Integer, ForeignKey('User.id'), nullable=False)
    # Relación de 1 a 1 entre usuarios en el sistema de seguimiento
    user_from = relationship('User', foreign_keys=[user_from_id])
    user_to = relationship('User', foreign_keys=[user_to_id])


class Post(Base):
    __tablename__ = 'Post'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('User.id'), nullable=False)
    # Relación N a 1 (Un post pertenece a un usuario)
    user = relationship('User', back_populates='post')
    # Relación 1 a N con Coment (Un post puede tener varios comentarios)
    coments = relationship('Coment', back_populates='post')
     # Relación 1 a N con Media (Un post puede tener varios medios)
    media = relationship('Media', back_populates='post')


class Media(Base):
    __tablename__ = 'Media'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('Post.id'), nullable=False)
    type = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    # Relación N a 1 (Un medio pertenece a un post)
    post = relationship('Post', back_populates='media')


class Coment(Base):
    __tablename__ = 'Coment'
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey('User.id'), nullable=False)
    post_id = Column(Integer, ForeignKey('Post.id'), nullable=False)
    comment_text = Column(String(250), nullable=False)
    # Relación N a 1 (Un comentario pertenece a un autor/usuario)
    author = relationship('Post', back_populates='coments')
    # Relación N a 1 (Un comentario pertenece a un post)
    post = relationship('Post', back_populates='comments')


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
