from application import db
from application.models import Base
from sqlalchemy.sql import text

recipe_ingredient = db.Table("recipeingredient", 
    db.Column("recipe_id", db.Integer, db.ForeignKey("recipe.id")),
    db.Column("ingredient_id", db.Integer, db.ForeignKey("ingredient.id")))

class Recipe(Base):

    name = db.Column(db.String(144), nullable=False)
    difficult = db.Column(db.String(144), nullable=False)
    event = db.Column(db.String(144), nullable=False)
    text = db.Column(db.String(1000), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)
    

    recipeingredients = db.relationship("Ingredient", secondary = recipe_ingredient,
        lazy="subquery", backref = db.backref("recipes", lazy = True))

    def __init__(self, name, text):
        self.name = name
        self.difficult = "Helppo"
        self.event = 'Arki'
        self.text = text
