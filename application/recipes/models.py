from application import db
from application.models import Base

class Recipe(Base):

    name = db.Column(db.String(144), nullable=False)
    difficult = db.Column(db.String(144), nullable=False)
    event = db.Column(db.String(144), nullable=False)
    text = db.Column(db.String(1000), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    

    def __init__(self, name, text):
        self.name = name
        self.difficult = "Helppo"
        self.event = 'Arki'
        self.text = text

