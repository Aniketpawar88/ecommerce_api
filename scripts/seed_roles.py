import os
import sys

BASE_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..")
)

sys.path.insert(0, BASE_DIR)

from app import create_app
from core.extensions import db
from models.role import Role

app = create_app()

with app.app_context():

    roles = [
        "ADMIN",
        "MANAGER",
        "USER"
    ]

    for role_name in roles:

        role = Role.query.filter_by(
            name=role_name
        ).first()

        if not role:

            db.session.add(
                Role(
                    name=role_name,
                    description=role_name
                )
            )

    db.session.commit()

    print("Roles seeded")