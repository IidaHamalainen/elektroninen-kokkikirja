from application import db
from application.models import Base

class Ingredient(Base):

    name = db.Column(db.String(144), nullable=False)

    def __init__(self, name):
        self.name = name
        self.id = id