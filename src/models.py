import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__= 'user'
    id = Column(Integer, primary_key = True)
    name = Column(String(120))
    email = Column(String(250))
    nickname = Column(String(120))

class Post(Base):
    __tablename__= 'post'
    id = Column(Integer, primary_key = True)
    title = Column(String(120))
    img = Column(String(250))
    comments = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

class Comment(Base):
    __tablename__= 'comment'
    id = Column(Integer, primary_key = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))
    comment = Column(String(250))
    user = relationship(User)
    post = relationship(Post)

class Friendship(Base):
    __tablename__= 'friendship'
    id = Column(Integer, primary_key=True)
    following_user = Column(Integer)
    follower_user = Column(Integer)
    Timestamp = Column(Integer)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
