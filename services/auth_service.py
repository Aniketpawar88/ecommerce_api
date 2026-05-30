from core import logger
from repositories.user_repository import UserRepository
from core.security import hash_password
from core.security import verify_password
from flask_jwt_extended import create_access_token
from flask_jwt_extended import create_refresh_token

class AuthService:

    @staticmethod
    def register(data):

        existing_user = UserRepository.get_by_email(
            data["email"]
        )

        if existing_user:
            raise Exception(
                "User already exists"
            )

        data["password_hash"] = hash_password(
            data.pop("password")
        )

        user = UserRepository.create_user(
            data
        )

        return user
    
    @staticmethod
    def login(data):
        from core.logger import logger
        logger.info("User logged in")

        user = UserRepository.get_by_email(
            data["email"]
    )

        if not user:
            raise Exception(
                "Invalid credentials"
            )

        if not verify_password(
            data["password"],
            user.password_hash
        ):
            raise Exception(
                "Invalid credentials"
            )

        access_token = create_access_token(
            identity=user.id
        )

        refresh_token = create_refresh_token(
            identity=user.id
        )

        return {
            "access_token": access_token,
            "refresh_token": refresh_token
        }
    
    @staticmethod
    def get_profile(user_id):
        
        user = UserRepository.get_by_id(
            user_id
        )

        if not user:
            raise Exception(
                "User not found"
            )

        return {
            "id": user.id,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email
        }
   