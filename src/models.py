import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Friendship(Base):
    __tablename__= 'friendship'
    id = Column(Integer, primary_key=True)
    following_user = Column(Integer)
    follower_user = Column(Integer)
    Timestamp = Column(Integer)
    

class User(Base):
    __tablename__= 'user'
    id = Column(Integer, primary_key=True)
    Username = Column(String(250), nullable=False)
    email = Column(String(250))
    Birdhdate = Column(Integer)
    Address = Column(String(250))
    Status = Column(String(250))
    Interests = Column(String(250))
    friendship_id = Column(Integer, ForeignKey('friendship.id'))
    friendship = relationship(Friendship)  

class Reaction(Base):
    __tablename__= 'reaction'
    id = Column(Integer, primary_key=True)
    Photo = Column(Integer, nullable=False)
    Reaction = Column(String(250))
    Reacting_user = Column(String(250))
    Timestamp = Column(Integer)
    

class Photo(Base):
    __tablename__= 'photo'
    id = Column(Integer, primary_key=True)
    Username = Column(String(250))
    Timestamp = Column(String(250))
    Location = Column(String(250))
    User_id = Column(Integer, ForeignKey('user.id'))
    User = relationship(User)
    Reaction_id = Column(Integer, ForeignKey('reaction.id'))
    Reaction = relationship(Reaction)
 

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
