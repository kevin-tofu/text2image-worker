# text2image-worker

## SetUp

### Redis & RabbitMQ Preparation

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
