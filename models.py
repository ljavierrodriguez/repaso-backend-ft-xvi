from email.policy import default
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    is_active = db.Column(db.Boolean(), default=True)
    avatar = db.Column(db.String(200), default="")
    profile = db.relationship('Profile', uselist=False)
    
    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "is_active": self.is_active,
            "avatar": self.avatar
        }
        
    def save(self):
        db.session.add(self)
        db.session.commit()
        
    def update(self):
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        
        
class Profile(db.Model):
    __tablename__ = 'profiles'
    id = db.Column(db.Integer, primary_key=True)
    resume = db.Column(db.String(200), default="")
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False, unique=True)