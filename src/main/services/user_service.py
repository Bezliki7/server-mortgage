from database.models import User
from database.init import db

class UserService:
    @staticmethod
    def add_user(username, email):
        new_user = User(username=username, email=email)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    @staticmethod
    def get_all_users():
        return User.query.all()