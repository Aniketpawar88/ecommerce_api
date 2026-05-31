import uuid

import boto3

from core.s3_config import (
    AWS_REGION,
    AWS_S3_BUCKET
)

s3_client = boto3.client(
    "s3",
    region_name=AWS_REGION
)


class S3Service:

    @staticmethod
    def upload_file(
        file,
        folder
    ):

        extension = file.filename.split(".")[-1]

        filename = (
            f"{uuid.uuid4()}.{extension}"
        )

        key = (
            f"{folder}/{filename}"
        )

        s3_client.upload_fileobj(
            file,
            AWS_S3_BUCKET,
            key,
            ExtraArgs={
                "ContentType":
                file.content_type
            }
        )

        return key