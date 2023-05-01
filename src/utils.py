import PIL
import io
from src.config import config_org as cfg
from src.logconf import mylogger
logger = mylogger(__name__)


def post_image_http(
    image: PIL.Image,
    **params
):
    
    import requests

    logger.info(f"task_id: {params['task_id']}")
    image_extention = params['image_extention'] if 'png' in params.keys() else 'png'
    image_quality = params['image_quality'] if 'image_quality' in params.keys() else 100
    file_in_memory = io.BytesIO()
    image.save(file_in_memory, image_extention, quality=image_quality)
    file_in_memory.seek(0)

    file = {
       'image': (
            f"{params['prompt']}.{image_extention}",
            file_in_memory.getvalue(),
            f'image/{image_extention}'
        )
    }
    res = requests.post(
        url=cfg.producer_url,
        files=file,
        params=dict(task_id=params['task_id'])
    )


def post_image_minio(
    image: PIL.Image,
    **params
):

    from minio import Minio

    logger.info(f"task_id: {params['task_id']}")
    image_extention = params['image_extention'] if 'png' in params.keys() else 'png'
    image_quality = params['image_quality'] if 'image_quality' in params.keys() else 100
    file_in_memory = io.BytesIO()
    image.save(file_in_memory, image_extention, quality=image_quality)
    file_in_memory.seek(0)
    minio_object_name = f"{params['task_id']}.{image_extention}"

    minio_secure = False if cfg.minio_secure is None else cfg.minio_secure
    minio_client = Minio(
        cfg.minio_url,
        access_key=cfg.minio_access_key,
        secret_key=cfg.minio_secret_key,
        secure=minio_secure
    )

    minio_client.put_object(
        bucket_name=cfg.minio_bucket_name,
        object_name=minio_object_name,
        data=file_in_memory.getvalue(),
        length=len(file_in_memory.getvalue()),
        content_type=f"image/{image_extention}"
    )

    
