from application import db
from application.models import Base
from sqlalchemy.sql import text

class Ingredient(Base):

    name = db.Column(db.String(144), nullable=False)

    def __init__(self, name):
        self.name = name

    def get_id(self):
        return self.id

    @staticmethod
    def most_used():
        stmt = text("SELECT Ingredient.id, Ingredient.name, COUNT(Recipeingredient.recipe_id) AS rcount FROM Ingredient"
                    " LEFT JOIN Recipeingredient ON Recipeingredient.ingredient_id = Ingredient.id"
                    " GROUP BY Ingredient.id"
                    " ORDER BY rcount DESC"
                    " LIMIT 8")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "count":row[2]})

        return response