import time
from datetime import datetime
import celery
from src.diffuser import diffuser_host
from src.config import config_org as cfg
from src.logconf import mylogger
logger = mylogger(__name__)

from src import utils


app = celery.Celery(
    __name__,
    broker=cfg.rabbitmq_url,
    backend=cfg.redis_url
)

# broker='redis://localhost:6379/0'
# app.conf.result_backend = 'redis://localhost:6379/0'

host = diffuser_host(cfg)


@app.task(name="prompt", bind=True)
def prompt(self, *args, **kwargs):

    params = kwargs
    params['task_id'] = self.request.id

    if params['test'] != 1:
        # for production
        logger.info(params['prompt'])
        self.update_state(
            state='PROGRESS',
            meta=dict(
                task_id=params['task_id'],
                timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                status='generating'
            )
        )
        image = host.generate_image(**params)


        self.update_state(
            state='PROGRESS',
            meta=dict(
                task_id=params['task_id'],
                timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                status='posting'
            )
        )
        utils.post_image_http(image, **params)

    else:
        #
        # for testing
        #
        from PIL import Image
        image = Image.open('./temp/a photo of an astronaut riding a horse on mars.png')

        for loop in range(10):
            time.sleep(5)
            self.myloop = loop
            self.update_state(
                state='PROGRESS',
                meta=dict(
                    current=loop,
                    total=10,
                    timestamp=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                )
            )

