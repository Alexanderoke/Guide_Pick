from app import db



class Guide(db.Model):
    id = db.Column(db.Integer, primary_key=True)    
    Name = db.Column(db.String(20), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    password = db.Column(db.String(60), nullable=False)
    languages= db.column(db.string(16), nullable=False)
    location = db.column(db.String(150), unique=False )
    skill_set = db.column(db.string(140),nullable=False)
    price= db.column(db.String(100))
    reviews = db.relationship('Review', backref='guide', lazy=True)