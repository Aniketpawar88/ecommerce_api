from flask import Blueprint

auth_bp = Blueprint(
    "auth",
    __name__,
    url_prefix="/api/v1/auth"
)

from api.v1.auth import routes