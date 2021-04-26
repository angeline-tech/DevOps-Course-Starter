# DevOps Apprenticeship: Project Exercise

## Running the App

There are a few options for running the application:
* [Virtual Environment with Python & Poetry](VENV.md) (Dev Environment - Flask)
* [Virtual Machine with Vagrant](Vagrant.md) (Dev Environment - Flask)
* [Docker Containers](Docker.md) (Dev Environment - Flask & Prod Environment - Gunicorn)

All three options require you to have a valid .env file. 

## Creating a valid .env file

You need to create a `.env` file from the `.env.template` to store local configuration options. This is a one-time operation on first setup:

```bash
$ cp .env.template .env  # (first time only)
```

The `.env` file is used by flask to set environment variables when running `flask run`. This enables things like development mode (which also enables features like hot reloading when you make a file change). There's also a [SECRET_KEY](https://flask.palletsprojects.com/en/1.1.x/config/#SECRET_KEY) variable which is used to encrypt the flask session cookie.

You'll need to add some information for the [Trello API](https://developer.atlassian.com/cloud/trello/rest/api-group-actions/). 

* `TRELLO_API_KEY`: API Key
* `TRELLO_TOKEN`: API Token
* `TRELLO_TO_DO`: idList to use for "To-Do" cards
* `TRELLO_IN_PROGRESS`: idList to use for "In" Progress cards
* `TRELLO_DONE`: idList to use for "Done" Cards

## Tests

### Prerequisites

* Geckodriver
* Firefox
* Add the path to the GeckoDriver Executable your `.env` file (`GECKO_PATH`)

### Running the Tests

To run tests run the following command. 
```bash
$ poetry run pytest tests
```
This will run any test defined in a function
matching the pattern ``test_*`` or ``*_test``, in any file matching the same patterns, in the ``tests`` directory.