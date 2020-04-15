from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/reviewDb'
db = SQLAlchemy(app)


user_reviews = db.Table('user_reviews',
    db.Column('review_id', db.Integer, db.ForeignKey('reviews.id'), primary_key=True),
    db.Column('restaurant_id', db.Integer, db.ForeignKey('restaurants.id'), primary_key=True)
)

class Restaurant(db.Model):
    __tablename__ = "restaurants"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    menu = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    phone = db.Column(db.String, nullable=False)

    # reviews = db.relationship('Review', backref='restaurant', lazy=True)

    reviews = db.relationship("Review", 
    secondary=user_reviews, 
    lazy="subquery", 
    backref=db.backref("user_reviews", lazy=True)
    )

    def __refr__(self):
        return f'Restaurant(id={self.id}, name="{self.name}", menu="{self.menu}", location="{self.location}", phone={self.phone})'
    
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)

    reviews = db.relationship('Review', backref='owner', lazy=True)

    def __repr__(self):
        return f'User(id={self.id}, email="{self.email}", name="{self.name}")'

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    header = db.Column(db.String(150), unique=True, nullable=False)
    body = db.Column(db.String, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete='SET NULL'))

    def __repr__(self):
        return f'Post(id={self.id}, header="{self.header}", body="{self.body}", owner_id="{self.owner_id}")'

    def as_dict(self):
        return {
            'id': self.id,
            'header': self.header,
            'body': self.body,
            'owner': self.owner.as_dict(),
        }