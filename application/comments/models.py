from application import db
from application.models import Base

class Comment(Base):

    comment_text = db.Column(db.String(250), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.id'), nullable=False)

    def __init__(self, comment_text):
        self.comment_text = comment_text

    
        