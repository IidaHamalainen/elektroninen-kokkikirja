from application import db
from application.models import Base
from sqlalchemy.sql import text

class User(Base):

    __tablename__ = "account"

    name = db.Column(db.String(144), nullable=False)
    username = db.Column(db.String(144), nullable=False)
    password = db.Column(db.String(144), nullable=False)
    user_role = db.Column(db.String(15), nullable=False)
    
    recipes = db.relationship("Recipe", backref='account', lazy=True)
    comments = db.relationship("Comment", backref='account', lazy=True)

    def __init__(self, name, username, password, user_role):
        self.name = name
        self.username = username
        self.password = password
        self.user_role = "USER"
  
    def get_id(self):
        return self.id

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def roles(self):
        return ["USER"]
    
    
    #yhteenvetokyselyt

    @staticmethod
    def users_recipes():
        stmt = text("SELECT Account.id, Account.name, COUNT(Recipe.id) FROM Account"
                    " LEFT JOIN Recipe ON Recipe.account_id = Account.id"
                    " GROUP BY Account.id")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id":row[0], "name":row[1], "count":row[2]})

        return response