from models.user import User
from core.extensions import db


class UserRepository:

    @staticmethod
    def get_by_email(email):
        return User.query.filter_by(
            email=email,
            is_deleted=False
        ).first()

    @staticmethod
    def create_user(data):
        user = User(**data)

        db.session.add(user)
        db.session.commit()

        return user
    
    @staticmethod
    def get_by_id(user_id):
        return User.query.filter_by(
            id=user_id,
            is_deleted=False
        ).first()