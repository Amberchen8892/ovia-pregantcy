from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin
from flask_dance.consumer.storage.sqla import OAuthConsumerMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import func



db = SQLAlchemy()


# class User(UserMixin, db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String, nullable=False)


class User(UserMixin, db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String) 
    last_period= db.Column(db.String)
    profile = db.relationship("Profile", backref='users', lazy=True, uselist=False)
    posts = db.relationship('Posts', backref='users', lazy='dynamic')
    comments = db.relationship('Comments',cascade="all, delete-orphan", backref='users', lazy='dynamic')


    def set_password(self,password):
        self.password = generate_password_hash(password)
    def check_password_hash(self, password):
        return check_password_hash(self.password, password)

    
class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name= db.Column(db.String) 
    last_name= db.Column(db.String) 
    profile_url= db.Column(db.String, default="https://image.flaticon.com/icons/svg/149/149072.svg",nullable=False)
    cover_url= db.Column(db.String, default="https://images.unsplash.com/photo-1490367605959-06955305859b",nullable=False)
   
    due_date= db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    
class Posts (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    body = db.Column(db.String, nullable=False)
    created = db.Column(db.DateTime)
    updated = db.Column(db.DateTime)
    view_count= db.Column(db.Integer, default=0)
    author = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    comments = db.relationship('Comments',cascade="all, delete-orphan", backref="posts", lazy="dynamic")
class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String, nullable=False)
    created = db.Column(db.DateTime, nullable=False)
    updated = db.Column(db.DateTime)
    author = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    post = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)

class OAuth(OAuthConsumerMixin, db.Model):
    provider_user_id = db.Column(db.String(256), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    user = db.relationship(User)


class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uuid = db.Column(db.String, unique=True)
    user_id = db.Column(db.Integer, db.ForeignKey(User.id), nullable=False)
    user = db.relationship(User)

class Pregnancybyweeks (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    intro = db.Column(db.String, nullable=False)
    mickey =  db.Column(db.String, nullable=False)
    mom =  db.Column(db.String, nullable=False)
    img_url = db.Column(db.String, nullable=False)
    source =  db.Column(db.String, nullable=False)
    reviewby =  db.Column(db.String, default= "Dr.Jamie Lo" ,nullable=False)
    week= db.Column(db.Integer)
class Symtoms (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    body = db.Column(db.String, nullable=False)
    img_url = db.Column(db.String, nullable=False)
    source =  db.Column(db.String, nullable=False)
    reviewby =  db.Column(db.String, default= "Dr.Jamie Lo" ,nullable=False)
    week= db.Column(db.Integer)
class Nutrition (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    intro = db.Column(db.String)
    body = db.Column(db.String, nullable=False)
    img_url = db.Column(db.String, nullable=False)
    source =  db.Column(db.String, nullable=False)
    reviewby =  db.Column(db.String, default= "Dr.Jamie Lo" ,nullable=False)
    week= db.Column(db.Integer)

class Excercises (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    body = db.Column(db.String, nullable=False)
    img_url = db.Column(db.String, nullable=False)
    source =  db.Column(db.String, nullable=False)
    reviewby =  db.Column(db.String, default= "Dr.Jamie Lo" ,nullable=False)
    week= db.Column(db.Integer)
class Losses (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    body = db.Column(db.String, nullable=False)
    img_url = db.Column(db.String, nullable=False)
    source =  db.Column(db.String, nullable=False)
    week= db.Column(db.Integer)
class Lifestyles (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    body = db.Column(db.String, nullable=False)
    img_url = db.Column(db.String, nullable=False)
    source =  db.Column(db.String, nullable=False)
    week= db.Column(db.Integer)
class Plainning (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    body = db.Column(db.String, nullable=False)
    img_url = db.Column(db.String, nullable=False)
    source =  db.Column(db.String, nullable=False)
class Laboranddelivery (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    body = db.Column(db.String, nullable=False)
    img_url = db.Column(db.String, nullable=False)
    source =  db.Column(db.String, nullable=False)
class Baby (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    body = db.Column(db.String, nullable=False)
    img_url = db.Column(db.String, nullable=False)
    week= db.Column(db.Integer)
    intro= db.Column(db.String)

class Intro (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    body = db.Column(db.String, nullable=False)
    img_url = db.Column(db.String, nullable=False)
    week= db.Column(db.Integer)








# setup login manager
login_manager = LoginManager()
# login_manager.login_view = "facebook.login"


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# verify token
@login_manager.request_loader
def load_user_from_request(request):
    api_key = request.headers.get('Authorization')
    print('================')
    if api_key:
        print('Hi Phuong heres the apikey', api_key)
        api_key = api_key.replace('Token ', '', 1)
        print('======', api_key)
        token = Token.query.filter_by(uuid=api_key).first()
        if token:
            return token.user

    return None
