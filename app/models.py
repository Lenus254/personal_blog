from datetime import datetime
from app import db, login_manager
from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash,check_password_hash


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):

    __tablename__ = 'users'
    
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    posts = db.relationship('Post',backref = 'user',lazy="dynamic")
    comments = db.relationship('Comment',backref = 'user',lazy = "dynamic")
    bio = db.Column(db.String(255))
    password_secure = db.Column(db.String(255))
    
    
    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)


    
    def __repr__(self):
        return f'User {self.username}'
    

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255))
    posted_date = db.Column(db.DateTime, default=datetime.utcnow)
    content = db.Column(db.Text)
    category = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment', backref='post', lazy=True)
    

    
    def __repr__(self):
        return f"Post('{self.title}', '{self.posted_date}', '{self.category}')"
    

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(255))
    comment = db.Column(db.Text, )
    posted_date = db.Column(db.DateTime, default=datetime.utcnow, )
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), )
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    
    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comment(cls,id):
        comments = Comment.query.filter_by(post_id=id).all()
        return comments
    
    def __repr__(self):
        return f"Comment('{self.comment}', '{self.posted_date}')"
    
    
class Quote:
    '''
    Quote class to define Quote Objects
    '''

    def __init__(self, id, author, quote, permalink):
        self.id = id
        self.author = author
        self.quote = quote
        self.permalink = permalink