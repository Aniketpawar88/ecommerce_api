from core.extensions import db
from models.base import BaseModel


class User(BaseModel):

    __tablename__ = "users"

    first_name = db.Column(
        db.String(100),
        nullable=False
    )

    last_name = db.Column(
        db.String(100),
        nullable=False
    )

    email = db.Column(
        db.String(255),
        unique=True,
        nullable=False,
        index=True
    )

    password_hash = db.Column(
        db.String(255),
        nullable=False
    )

    is_active = db.Column(
        db.Boolean,
        default=True
    )

    role_id = db.Column(
        db.String(36),
        db.ForeignKey("roles.id")
    )