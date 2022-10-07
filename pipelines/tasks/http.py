import requests
from botocore.client import BaseClient

from pipelines import DEFAULT_S3_BUCKET


def download_and_store_to_s3(
    url: str,
    filename: str,
    s3: BaseClient,
    bucket=DEFAULT_S3_BUCKET,
) -> str:
    """Download URL content and store it on s3."""
    response = requests.get(url, timeout=2)
    response.raise_for_status()

    if len(response.content) == 0:
        raise ValueError("No data to save")

    s3.put_object(Bucket=bucket, Key=filename, Body=response.content)
    return f"s3://{bucket}/{filename}"
