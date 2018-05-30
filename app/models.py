import os, jwt
from . import login_manager
from . import db, admin
from flask_admin.contrib.sqla import ModelView
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, current_user
from datetime import datetime
from time import time

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(48), unique = True, index=True)
    email = db.Column(db.String(48),unique=True, index = True)
    group = db.Column(db.String())
    hash_pass = db.Column(db.String(255)) 

    posts = db.relationship('Post', backref='user', lazy='dynamic')
    is_admin = db.Column(db.Boolean)
    comments = db.relationship('Comment', backref='user', lazy='dynamic')

    @property
    def password(self):
        raise AttributeError("You cannot read password attribute")

    @password.setter
    def password(self,password):
        self.hash_pass = generate_password_hash(password)
    
    def set_password(self,password):
        self.hash_pass = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.hash_pass,password)  
    
    def get_reset_password_token(self, expires_in=1800):
        return jwt.encode({'reset_password':self.id, 'exp':time()+expires_in}, os.environ.get('SECRET_KEY'), algorithm='HS256').decode('utf-8')
    
    @staticmethod
    def verify_reset_password(token):
        try:
            id = jwt.decode(token, os.environ.get('SECRET_KEY'),algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)  


class Post(UserMixin, db.Model):
    """ 
    class modelling the posts
    """

    __tablename__ = 'posts'

    # add columns
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    post = db.Column(db.String)
    image_name = db.Column(db.String)
    image_url = db.Column(db.String)
    timeposted = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    comments = db.relationship('Comment', backref='post', lazy='dynamic')

    def __repr__(self):
        return f'Post{self.post}'


# Role class 
class Role(UserMixin, db.Model):
    """ 
    class modelling the role of each user
    """

    __tablename__ = "roles"

    # add columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    

    def __repr__(self):
        return f'Post{self.name}'

# comments
class Comment(UserMixin, db.Model):
    """ 
    User comment model for each post
    """

    __tablename__ = "comments"

    # add columns
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.String)
    commenter = db.Column(db.String)
    
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'))
    
    def __repr__(self):
        return f'Post{self.comment}'


class Subscribers(UserMixin, db.Model):

    __tablename__ = "subscribers"

    # add columns 
    id= db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True)

    def __repr__(self):
        return f'Subscribers{self.email}'

class MyModelView(ModelView):
    def is_accessible(self):
        return False

            

admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Post, db.session))
admin.add_view(ModelView(Comment, db.session))
admin.add_view(ModelView(Subscribers, db.session))        