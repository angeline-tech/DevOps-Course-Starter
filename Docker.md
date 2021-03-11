# Docker 

## Prerequisites
* [Docker](https://docs.docker.com/get-docker/) (Should also include docker-compose)
* A valid .env file (See [README.md](README.md))

## Running a Dev Container

The dev container uses `Flask` to serve the app so you will be able to
* Hot reload app on save without rebuilding the container
* Use Flask's debugging/developer mode to provide detailed loggin and feedback

To run the dev container you first need to build an image from the [Dockerfile](Dockerfile) using the development target. To do this you can run: 

```bash
$ docker build --target development --tag todo_app:dev .
```
Once you have your image you can start the container by running:
```bash
$ docker run --env-file .env -p 5000:5000 --volume $(pwd)/todo_app:/todo_app/todo_app  todo_app:dev 
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Running a Prod Container

This prod container uses Gunicorn to serve the app and is a more production like environment

To run the prod container you first need to build an image from the [Dockerfile](Dockerfile) using the production target. To do this you can run: 

```bash
$ docker build --target production --tag todo_app:prod .
```
Once you have your image you can start the container by running:
```bash
$ docker run --env-file .env -p 5000:5000 todo_app:prod 
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.

## Using Docker Compose to Run Everything

You can use docker-compose to simplify the process of starting the containers. To start both containers (dev and prod) you can simply run 

```bash
$ docker-compose up
```

The prod container will be running on port 5000 [`http://localhost:5000/`](http://localhost:5000/) 

The dev container will be running on port 8080 [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view production app.

The forwarded ports can be changed in the [docker-compose file](docker-compose.yml) to suit your needs