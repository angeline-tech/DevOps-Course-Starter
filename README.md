# DevOps Apprenticeship: Project Exercise

## Creating a Development Environment

In order to create a working environment you need to create a ``.env`` file to store the necessary Environment Variables and then use one of the two following two approaches.
* Virtual Environment with Python & Poetry
* Virtual Machine with Vagrant

## Environment Variables

You'll also need to clone a new `.env` file from the `.env.tempalate` to store local configuration options. This is a one-time operation on first setup:

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


## Virtual Environment with Python & Poetry

The project uses poetry for Python to create an isolated environment and manage package dependencies. You can either create use Vagrant to create a VM for your development environment or you can create an isolated environment directly by manually installing Python (3.7+) and [poetry](https://python-poetry.org/docs/#system-requirements)

 To prepare your system, ensure you have an official distribution of Python version 3.7+ and install poetry using one of the following commands (as instructed by the [poetry documentation](https://python-poetry.org/docs/#system-requirements)):

### Poetry installation (Bash)

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

### Poetry installation (PowerShell)

```powershell
(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python
```

### Dependencies

The project uses a virtual environment to isolate package dependencies. To create the virtual environment and install required packages, run the following from your preferred shell:

```bash
$ poetry install
```

### Running the App

Once the all dependencies have been installed, start the Flask app in development mode within the poetry environment by running:
```bash
$ poetry run flask run
```

You should see output similar to the following:
```bash
 * Serving Flask app "app" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with fsevents reloader
 * Debugger is active!
 * Debugger PIN: 226-556-590
```
Now visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.



## Virtual Machine with Vagrant


You can also run the app using Vagrant to create a Virtual Machine (VM). This allows you to easily create a developer environment without worrying about dependencies like Python or Poetry

### Prerequisites
* [Vagrant](https://www.vagrantup.com/)
* A Hypervisor (We recommend [VirutalBox](https://www.virtualbox.org/))

### Starting the app on the VM
There are two ways to start the app on the VM:
* ``vagrant up ``- Starts your VM, creating and provisioning your it automatically required. It also automatically launches the To Do App when the setup is complete.
* ``vagrant ssh`` - Allows you to connect to the VM and interact with it through a shell. Once you are connected you can run ``cd /vagrant && poetry run flask run``). 

You van verify the flask server is running on the VM by logging in and running the command
``curl localhost:5000/heartbeat``

You can then visit [`http://localhost:5000/`](http://localhost:5000/) in your web browser to view the app.


### Managing the VM
The VM can be managed using vagrant's CLI commands. Some useful ones are:
* ``vagrant provision`` - Runs any VM provisioning steps specified in the Vagrantfile. Provisioning steps are one-off operations that adjust the system provided by the box.
* ``vagrant suspend`` - Suspends any running VM. The VM will be restarted on the next vagrant up command.
* ``vagrant destroy`` - Destroys the VM. It will be fully recreated the next time you run vagrant up.


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