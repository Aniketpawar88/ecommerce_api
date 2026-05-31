from flask import Flask

from core.extensions import db
from core.extensions import jwt
from core.extensions import migrate
from core.config import Config
from core.extensions import limiter
def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    jwt.init_app(app)

    migrate.init_app(app, db)
    limiter.init_app(app)
     # Register Blueprints
    from api.v1.auth.routes import auth_bp
    from core.error_handlers import register_error_handlers
    from api.v1.files.upload.routes import files_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(files_bp)
    register_error_handlers(app)
    from models import User, Role
    
    return app