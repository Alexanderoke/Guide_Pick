from flask_sqlalchemy import SQLAlchemy


db=SQLAlchemy()

class Guide(db.Model):
    id = db.Column(db.Integer, primary_key=True)    
    Name = db.Column(db.String(20), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    languages= db.column(db.String(16))
    location = db.column(db.String(150))
    price= db.column(db.String(100))
    # reviews = db.relationship('Review', backref='guide', lazy=True)