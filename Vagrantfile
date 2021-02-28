Vagrant.configure("2") do |config|

  config.vm.box = "hashicorp/bionic64"

  config.vm.provision "shell", privileged: false, path: "vagrant_provision.sh"
  
  config.trigger.after :up do |trigger|
    trigger.name = "Launching App"
    trigger.info = "Running the TODO app setup script" 
    trigger.run_remote = {privileged: false, path: "vagrant_trigger.sh"}
    end

end
