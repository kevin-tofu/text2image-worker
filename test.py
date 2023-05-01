from src.config import config_org as config
from src.diffuser import diffuser_host

if __name__ == '__main__':

    print('start')
    print(config, type(config))
    # prompt = "a photo of an astronaut riding a horse on mars"
    prompt = "A newborn human baby biting into a fish as hard as he can"

    kwargs = dict(prompt=prompt)

    host = diffuser_host(config)
    image = host.generate_image(**kwargs)

    image.save(f"./temp/{prompt}.png")

    
