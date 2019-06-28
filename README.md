# Raspberry pi - OLED - Ansible - Kubernetes

Goal:
- Put a stack of *Raspberry Pi*'s to use
- Show information on *OLED display* like:
  - IP address
  - System load
  - Cats
- Get to know *Ansible*
- Learn *Markdown language*
- Learn *git*

## Use Markdown cheat sheet
As found [here](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

## Generate SSH key
To be deployed to all of the Raspberry Pi's. As my ssh key is already in place,
this will be described some other time...

## Install Ansible
Currently the Ansible playbooks are developed in Ubuntu 19.04, running in a 
virtual machine (Virtualbox). 

Install Ansible by following [these](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#latest-releases-via-apt-ubuntu) instructions:


````
$ sudo apt update
$ sudo apt install software-properties-common
$ sudo apt-add-repository --yes --update ppa:ansible/ansible
$ sudo apt install ansible
````

## Ansible inventory
As default, Ansible uses `/etc/ansible` for configuring the hosts/nodes. As I
want to learn Ansible without root permissions, I am aggregating inventory
sources with a directory, as described [here](https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html#using-multiple-inventory-sources)


