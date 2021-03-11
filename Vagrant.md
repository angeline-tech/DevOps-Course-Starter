## Creating a Dev Environment with Vagrant

Follow these instructions to create a local developer environment using Vagrant (creates a VM) 

### Prerequisites
* [Vagrant](https://www.vagrantup.com/)
* A Hypervisor (We recommend [VirutalBox](https://www.virtualbox.org/))
* A valid .env file (See [README.md](README.md))

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
