Vagrant.configure("2") do |config|
  config.vm.box = "centos/stream9"
  config.vm.box_version = "20250922.0"
  config.vm.network "public_network"
#  config.disksize.size = '50GB'
  config.vm.provider "virtualbox" do |v|
    v.memory = 4096
    v.cpus = 2
  end

  config.vm.provision "shell", inline: <<-SHELL
    cp /vagrant/vaultpass /home/vagrant/vaultpass
    chmod 644 /home/vagrant/vaultpass
  SHELL

  config.vm.provision "shell", inline: <<-SHELL
    echo 'Defaults:vagrant !requiretty' | sudo tee /etc/sudoers.d/vagrant-nopty
    echo 'vagrant ALL=(ALL) NOPASSWD:ALL' | sudo tee /etc/sudoers.d/vagrant-nopasswd
    sudo chmod 0440 /etc/sudoers.d/vagrant-nopty
    sudo chmod 0440 /etc/sudoers.d/vagrant-nopasswd
  SHELL
  
  config.vm.provision "ansible_local" do |ansible|
    ansible.become = true
    ansible.become_user = "root"
    ansible.playbook = "infrastructure/ansible/dependencies.yml"
    ansible.inventory_path = "infrastructure/ansible/inventory.ini"
    ansible.limit = "localhost.localdomain"
  end

  config.vm.provision "ansible_local" do |ansible|
    ansible.become = true
    ansible.become_user = "root"
    ansible.playbook = "infrastructure/ansible/owaspjuiceshop.yml"
    ansible.inventory_path = "infrastructure/ansible/inventory.ini"
    ansible.limit = "localhost.localdomain"
  end

end
