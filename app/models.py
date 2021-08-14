from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Pitch(db.Model):
    __tablename__ = 'pitches'
    pitch_id = db.Column(db.Integer,primary_key = True)
    pitch_title = db.Column(db.String)
    pitch_content = db.Column(db.String)
    posted = db.Column(db.Time,default=datetime.utcnow())
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    category= db.Column(db.String)
    up_vote = db.Column(db.Integer, default=0)
    down_vote = db.Column(db.Integer, default = 0)
    comments = db.relationship('Comment',backref = 'comment',lazy="dynamic")




    def save_pitch(self):
        db.session.add(self)
        db.session.commit()



    @classmethod
    def get_pitches(cls,pitch_id):

        pitches = Pitch.query.filter_by(pitch_id=pitch_id).all()
        return pitches

class Comment(db.Model):
    
    __tablename__ = 'comments'
    id = db.Column(db.Integer,primary_key = True)
    pitch_id = db.Column(db.Integer, db.ForeignKey("pitches.pitch_id"))
    pitch_comment = db.Column(db.String)
    posted = db.Column(db.Time,default=datetime.utcnow())
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))



    def save_comment(self):
        db.session.add(self)
        db.session.commit()



    @classmethod
    def get_comments(cls,pitch_id):

        comments = Comment.query.filter_by(pitch_id=pitch_id).all()
        return comments



class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))
    pitch = db.relationship('Pitch',backref = 'user',lazy = "dynamic")
    comment = db.relationship('Comment',backref = 'user',lazy = "dynamic")

    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)


    def verify_password(self,password):
        print(self.password_secure)
        return check_password_hash(self.password_secure,password)

        
    def __repr__(self):
        return f'User {self.username}'


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")


    def __repr__(self):
        return f'User {self.name}'

