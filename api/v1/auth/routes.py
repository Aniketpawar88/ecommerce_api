from flask import Blueprint
from flask import request
from schemas.auth_schema import (RegisterSchema, LoginSchema)
from services.auth_service import AuthService
from flask_jwt_extended import jwt_required
from flask_jwt_extended import get_jwt_identity
from core.extensions import limiter
from core.logger import logger

auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/api/v1/auth"
)


@auth_bp.route("/health")
def health():
    logger.info("Health API called")

    return {
        "success": True,
        "message": "Auth Module Working"
    }

@auth_bp.route(
    "/register",
    methods=["POST"]
)
def register():

    schema = RegisterSchema()

    data = schema.load(
        request.get_json()
    )
    logger.info(f"Register API json:",{data})

    user = AuthService.register(
        data
    )

    return {
        "success": True,
        "message": "User registered",
        "user_id": user.id
    }, 201

@auth_bp.route(
    "/login",
    methods=["POST"]
)
@limiter.limit("5 per minute")
def login():
    

    schema = LoginSchema()

    data = schema.load(
        request.get_json()
    )
    logger.info(f"Rate limiting added for:",{data})
    result = AuthService.login(
        data
    )

    return {
        "success": True,
        **result
    }


@auth_bp.route(
    "/profile",
    methods=["GET"]
)
@jwt_required()
def profile():

    user_id = get_jwt_identity()

    data = AuthService.get_profile(
        user_id
    )

    return {
        "success": True,
        "data": data
    }