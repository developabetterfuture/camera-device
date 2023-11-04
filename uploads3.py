import boto3


class uploads3:
    BUCKET = ""
    config = {
        "aws_access_key_id": "",
        "aws_secret_access_key": "",
        "region_name": "eu-central-1",
        "endpoint_url": "",
    }


def upload_file(file_name, object_name=None):
    if object_name is None:
        object_name = file_name

    client = boto3.client("s3", **uploads3.config)
    client.upload_file(file_name, uploads3.BUCKET, object_name)


print("File uploaded successfully")
