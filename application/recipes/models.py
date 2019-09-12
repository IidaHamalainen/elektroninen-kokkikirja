from application import db

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())

    name = db.Column(db.String(144), nullable=False)
    difficult = db.Column(db.String(144), nullable=False)

    def __init__(self, name):
        self.name = name
        self.difficult = "helppo"
