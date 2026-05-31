from flask import Blueprint
from flask import request
from flask_jwt_extended import jwt_required

from core.constants import (
    ALLOWED_IMAGE_EXTENSIONS,
    MAX_FILE_SIZE
)
from services.s3_service import S3Service

files_bp = Blueprint(
    "files",
    __name__,
    url_prefix="/api/v1/files"
)


@files_bp.route(
    "/upload",
    methods=["POST"]
)
@jwt_required()
def upload():
    
    if "file" not in request.files:
        return {
            "success": False,
            "message": "File required"
        }, 400

    file = request.files["file"]
    file.seek(0, 2)
    file_size = file.tell()
    file.seek(0)

    if file_size > MAX_FILE_SIZE:
        return {
            "success": False,
            "message": "File exceeds 5MB limit"
        }, 400

    extension = (
        file.filename
        .split(".")[-1]
        .lower()
    )

    if extension not in ALLOWED_IMAGE_EXTENSIONS:        
        return {
            "success": False,
            "message": "Invalid file type"
        }, 400

    key = S3Service.upload_file(
        file=file,
        folder="users"
    )

    return {
        "success": True,
        "key": key
    }