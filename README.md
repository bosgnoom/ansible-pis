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

Hints for myself:
- As found [here](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

Steps done:
- Install Ansible
- Check which hosts are online --> poll.yml

Steps to be taken:
- Configure new hosts
  - 


## Generate SSH key
To be deployed to all of the Raspberry Pi's. As my ssh key is already in place,
this will be described some other time...


## Ansible
### Install Ansible
Currently the Ansible playbooks are developed in Ubuntu 19.04, running in a 
virtual machine (Virtualbox). 

Install Ansible by following [these](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#latest-releases-via-apt-ubuntu) instructions:


```
$ sudo apt update
$ sudo apt install software-properties-common
$ sudo apt-add-repository --yes --update ppa:ansible/ansible
$ sudo apt install ansible
```

### Ansible inventory
As default, Ansible uses `/etc/ansible` for configuring the hosts/nodes. As I
want to learn Ansible without running with root permissions, I am aggregating
inventory sources with a directory, as described [here](https://docs.ansible.com/ansible/latest/user_guide/intro_inventory.html#using-multiple-inventory-sources)


### Run Ansible
`ansible-playbook -i inventory poll.yml`


## Git 
At the moment I am using both my local git (running on my Synology NAS) and
my github account to store this work. Git can push to different servers as
described [here](https://gist.github.com/rvl/c3f156e117e22a25f242). Please 
remind the next time to create an empty repository on github, otherwise git
will complain.

```
git remote set-url --add --push origin git@github.com:muccg/my-project.git
git remote set-url --add --push origin git@bitbucket.org:ccgmurdoch/my-project.git
```

I ended up editing the `.git/config` file to match my local ssh url.


