Vagrant.configure("2") do |config|

  config.vm.box = "hashicorp/bionic64"

  config.vm.provision "shell", privileged: false, path: "vagrant_provision.sh"
  
  config.vm.network "forwarded_port", guest: 5000, host: 5000, auto_correct: true

  config.trigger.after :up do |trigger|
    trigger.name = "Launching App"
    trigger.info = "Running the TODO app setup script" 
    trigger.run_remote = {privileged: false, path: "vagrant_trigger.sh"}
    end

end
