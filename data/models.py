from db_alchemy import db
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from dataclasses import dataclass

class Influencer(db.Model):
    __tablename__ = 'influencer'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    platform = db.Column(db.String)
    category = db.Column(db.String)
    url = db.Column(db.String)
    reviews = relationship("Review", back_populates="influencer")

    def __init__(self, name, platform, category, url):
        self.name = name
        self.platform = platform
        self.category = category
        self.url = url

    def __repr__(self):
        return '<Influencer %r>' % self.id

    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'platform': self.platform, 'category': self.category, 'url': self.url}
    
class Review(db.Model):
    __tablename__ = 'review'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    url = db.Column(db.String)
    id_influencer = db.Column(db.Integer, ForeignKey('influencer.id'))
    transcript = db.Column(db.String)
    vote = db.Column(db.Integer)
    influencer = relationship("Influencer", back_populates="reviews")

    def __init__(self, name, url, id_influencer, transcript, vote):
        self.name = name
        self.url = url
        self.id_influencer = id_influencer
        self.transcript = transcript
        self.vote = vote

    def __repr__(self):
        return '<Review %r>' % self.id
    
    def to_dict(self):
        return {'id': self.id, 'name': self.name, 'url': self.url, 'id_influencer': self.id_influencer, 'transcript': self.transcript, 'vote': self.vote, 'name_influencer': self.influencer.name}
