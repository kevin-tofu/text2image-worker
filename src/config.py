import os
from typing import Optional
# from typing import NamedTuple
from dataclasses import dataclass

VERSION = os.getenv('VERSION', 'v0.0.1'),
AUTHOR = os.getenv('AUTHOR', 'kevin')

MODEL_ID = os.getenv('MODEL_ID', 'runwayml/stable-diffusion-v1-5')
MODEL_DEVICE = os.getenv('MODEL_DEVICE', 'cpu')
MODEL_PATH = os.getenv('MODEL_PATH', '../model')
# IMSIZE_H = os.getenv('IMSIZE_H', 512)
# IMSIZE_W = os.getenv('IMSIZE_W', 512)

RABBITMQ_URL = os.getenv('RABBITMQ_URL', 'amqp://localhost:6380')
REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
PRODUCER_URL = os.getenv('PRODUCER_URL', 'http://localhost:3333')


@dataclass(slots=True)
class Config():
    version: str
    author: str
    model_id: str
    model_path: str
    model_device: str
    rabbitmq_url: str
    redis_url: str
    producer_url: Optional[str]
    minio_url: Optional[str]
    minio_access_key: Optional[str]
    minio_secret_key: Optional[str]
    minio_bucket_name: Optional[str]
    minio_secure: Optional[str]
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
    PRODUCER_URL
)


if __name__ == '__name__':

    print(config_org)
