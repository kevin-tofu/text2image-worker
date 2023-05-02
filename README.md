# text2image-worker

## SetUp

### launch Redis & RabbitMQ

```bash
docker-compose -f docker/docker-compose.yml up -d
```

### Build using Docker

```bash

docker build . -t text2image-worker -f docker/Dockerfile

```

### Build using Poetry

```bash

poetry install

```

### How to Run using Docker

```bash
docker run -it -d --rm \
   -e RABBITMQ_URL=amqp://localhost:6380 \
   -e REDIS_URL=redis://localhost:6379/0 \
   --name worker \
   text2image-worker
```

### How to run using Poetry

```bash

poetry run python -m celery  -A tasks worker --loglevel=info --concurrency=1

```

## Environment Variables

| Name | type | Example | Description |
| --- | --- | --- | --- |
| VERSION | str | {COMMIT_SHA} |  |
| MANAGER | str | 'myname' |  |
| MODEL_ID | str | 'runwayml/stable-diffusion-v1-5' |  |
| MODEL_PATH | str | './model' |  |
| MODEL_DEVICE | str | 'cpu' |  |
| RABBITMQ_URL | str | 'amqp://localhost:6380' |  |
| REDIS_URL | str | 'redis://localhost:6379/0' |  |
| PRODUCER_URL | str | 'http://localhost:3333' |  |
| MINIO_URL | str | '' |  |
| MINIO_ACCESS_KEY | str | '' |  |
| MINIO_SECRET_KEY | str | '' |  |
| MINIO_BUCKET_NAME | str | '' |  |
| MINIO_SECURE | str | '' |  |
