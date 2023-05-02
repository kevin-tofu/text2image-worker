import os
from typing import Optional
# from typing import NamedTuple
from dataclasses import dataclass

VERSION = os.getenv('VERSION', 'v0.0.1'),
AUTHOR = os.getenv('AUTHOR', 'kevin')

MODEL_ID = os.getenv('MODEL_ID', 'runwayml/stable-diffusion-v1-5')
MODEL_PATH = os.getenv('MODEL_PATH', '../model')
MODEL_DEVICE = os.getenv('MODEL_DEVICE', 'cpu')

# IMSIZE_H = os.getenv('IMSIZE_H', 512)
# IMSIZE_W = os.getenv('IMSIZE_W', 512)

RABBITMQ_URL = os.getenv('RABBITMQ_URL', 'amqp://localhost:6380')
REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
PRODUCER_URL = os.getenv('PRODUCER_URL', 'http://localhost:3333')

MINIO_URL = os.getenv('MINIO_URL', None)
MINIO_ACCESS_KEY = os.getenv('MINIO_ACCESS_KEY', None)
MINIO_SECRET_KEY = os.getenv('MINIO_SECRET_KEY', None)
MINIO_BUCKET_NAME = os.getenv('MINIO_BUCKET_NAME', None)
MINIO_SECURE = os.getenv('MINIO_SECURE', None)


@dataclass(slots=True)
class Config():
    version: str
    author: str
    model_id: str
    model_path: str
    model_device: str
    rabbitmq_url: str
    redis_url: str
    producer_url: Optional[str] = None
    minio_url: Optional[str] = None
    minio_access_key: Optional[str] = None
    minio_secret_key: Optional[str] = None
    minio_bucket_name: Optional[str] = None
    minio_secure: Optional[str] = None
    # minio_object_name: Optional[str]
    # imsize_h: int
    # imsize_w: int

config_org = Config(
    VERSION,
    AUTHOR,
    MODEL_ID,
    MODEL_PATH,
    MODEL_DEVICE,
    RABBITMQ_URL,
    REDIS_URL,
    PRODUCER_URL,
    MINIO_URL,
    MINIO_ACCESS_KEY,
    MINIO_SECRET_KEY,
    MINIO_BUCKET_NAME,
    MINIO_SECURE
)


if __name__ == '__name__':

    print(config_org)
