# hellospeak-be
HelloSpeak API


# Table of contents

1. [Setup](#setup)
2. [Migrations](#migrations)
3. [API Documentation](#api-documentation)
4. [Production run](#production-run)
5. [Pre-commit](#pre-commit)


## Setup

- Create [poetry](https://python-poetry.org/docs/#installation) environment (using [pyenv](https://github.com/pyenv/pyenv#installation) to manage python version)

```shell
poetry env use python
```
or specific version if you don't use pyenv


- Login to poetry shell

```shell
poetry shell
```

- Install dev dependencies only for formatting and linting

```shell
poetry install --no-root --group dev
```

- Copy .env.example and change value if needed

```shell
cp .env.example .env
```

- Develop using docker for environment consistency
```shell
docker-compose -f docker/dev.docker-compose.yaml up -d
```

When add new library, build the docker image again

```shell
docker-compose -f docker/dev.docker-compose.yaml build
```

## Migrations

Access to docker container and run the migrations

```shell
docker exec -it hellospeak-api /bin/sh
```

```shell
python manage.py migrate
```

To create a new migration

```shell
python manange.py makemigrations app
```
## API Documentation

The API documentation is available at `http://localhost:8000/docs` endpoint.

## Production run

`docker-compose -f docker/docker-compose.yml up`

## Pre-commit

This project uses `pre-commit` hooks to run, at a minimum, `ruff` for linting the source code.

```shell
pre-commit install
```

it's usually a good idea to run the hooks against all the files when adding new hooks (usually pre-commit will only run on the changed files during git hooks)
```shell
pre-commit run --all-files
```
