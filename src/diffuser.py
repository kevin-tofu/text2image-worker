from PIL import Image
from src.config import Config
from diffusers import StableDiffusionPipeline
# import torch
from src.logconf import mylogger
logger = mylogger(__name__)

class diffuser_host():

    def __init__(self, cfg: Config):
        super().__init__()
        
        logger.info(cfg.model_id)
        logger.info(cfg.model_path)
        logger.info(cfg.model_device)
        # model_id = "runwayml/stable-diffusion-v1-5"
        pipe = StableDiffusionPipeline.from_pretrained(
            cfg.model_id,
            # torch_dtype=torch.float16,
            cache_dir=cfg.model_path
        )
        # self.pipe = pipe.to("cpu")
        self.pipe = pipe.to(cfg.model_device)

        # prompt = "a photo of an astronaut riding a horse on mars"
        

    
    def get_image(
        self,
        **kwargs
    ) -> Image:
        
        prompt = kwargs['prompt']
        image = self.pipe(prompt).images[0]
        # print(type(image))

        return image

