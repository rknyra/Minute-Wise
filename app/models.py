from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager



class User(UserMixin,db.Model):
    __tablename__='users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(70))
    email = db.Column(db.String(70))
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String)
    # pitches = db.relationship('Pitch',backref = 'user',lazy="dynamic")
    comments = db.relationship('Comment',backref = 'user',lazy="dynamic")

        
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')
    
    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)
    
    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)
    
    def __repr__(self):
        return f'User {self.username}'
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))


class Pitch(db.Model):
    __tablename__='pitches'
    id = db.Column(db.Integer,primary_key = True)
    pitch = db.Column(db.String(255))
    category = db.Column(db.String(255))
    # users_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    comments = db.relationship('Comment',backref = 'pitch',lazy="dynamic")
    
    def save_pitch(self):
        db.session.add(self)
        db.session.commit()
    
    # def get_comments(self):
    #     return Comment.query.filter_by(pitches_id=pitches.id).all()
    
    def __repr__(self):
        return f'{self.pitch}'
    
    
class Comment(db.Model):
    __tablename__='comments'
    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String(255))
    pitches_id = db.Column(db.Integer,db.ForeignKey('pitches.id'))
    users_id = db.Column(db.Integer,db.ForeignKey('users.id'))
  
    
    # def save_comment(self):
    #     db.session.add(self)
    #     db.session.commit()
    
    # def get_comments(self):
    #     return Comment.query.filter_by(pitches_id=pitches.id).all()
    
    def __repr__(self):
        return f"Comment('{self.comment}','{self.pitches_id}','{self.users_id}')"
    
