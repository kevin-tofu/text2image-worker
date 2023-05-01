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

    image_extention = params['image_extention'] if 'png' in params.keys() else 'png'
    image_quality = params['image_quality'] if 'image_quality' in params.keys() else 100
    file_in_memory = io.BytesIO()
    image.save(file_in_memory, image_extention, quality=image_quality)
    file_in_memory.seek(0)

    print(len(file_in_memory))
    # print(type(self))
    # print(self.request)
    # print(f'self.request.id: {self.request.id}')
    # print(f'task_id: {task_id}')

    file = {
       'image': (
            f"{params['prompt']}.{image_extention}",
            file_in_memory.getvalue(),
            f'image/{image_extention}'
        )
    }
    # res = requests.post(
    #     url=cfg.producer_url,
    #     files=file,
    #     params=dict(task_id='task_id')
    # )


def post_image_minio(
    image: PIL.Image,
    **params
):

    from minio import Minio

    image_extention = params['image_extention'] if 'png' in params.keys() else 'png'
    image_quality = params['image_quality'] if 'image_quality' in params.keys() else 100
    file_in_memory = io.BytesIO()
    image.save(file_in_memory, image_extention, quality=image_quality)
    file_in_memory.seek(0)

    minio_client = Minio(
        cfg.minio_url,
        access_key=cfg.minio_access_key,
        secret_key=cfg.minio_secret_key,
        secure=False # When to use SSL/TLS it is True
    )

    minio_client.put_object(
        bucket_name=cfg.minio_bucket_name,
        object_name=cfg.minio_object_name,
        data=file_in_memory.getvalue(),
        length=len(file_in_memory.getvalue()),
        content_type=f"image/{image_extention}"
    )

    pass