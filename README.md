# Raspberry pi - OLED - Ansible - Kubernetes


Goal:
- Put a stack of *Raspberry Pi's* to use
- Show information on *OLED display* like:
  - IP address
  - System load
  - Cats
- Get to know *Ansible*
- Learn *Markdown language*
- Learn *git*

Hints for myself:
- Markdown cheat sheet [here](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)


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


## Generate SSH key
To be deployed to all of the Raspberry Pi's. As my ssh key is already in place,
this will be described some other time...


## Ansible
Ansible will be used for:
- Set up the raspberry pi:
  - Install packages often used by me:
    - mc
    - python-pexpect (needed for...)
    - screen
    - build-essential
    - git
  - Boot the pi to CLI
  - Change the default password
  - Deploy the ssh key (login without password)
  - Set up networking: Will be based on the mac_address mapping (mac --> ip address)
    - dhcpcd.conf (for static ip address)
    - set hostname (/etc/hostname)
    - set hosts (/etc/hosts)
    - set dns nameserver (/etc/resolv.conf)
  - Change the GPU memory size to minimum (16MB)
  - Set the timezone
  
- Set up the OLED display:
  - Enable i2c (for the OLED display)
  - Install needed packages (apt)
    - python-dev
    - python-pip
    - python-imaging
    - python-smbus
  - Install needed python packages (pip)
    - RPI.GPIO
  - Install Adafruit's SSD1306 python driver
  - Show the catz
  
- Prepare for kubernetes:
  - cgroup
  - disable swap
  

### Install Ansible
Currently the Ansible playbooks are developed in Ubuntu 19.04, running in a 
virtual machine (Virtualbox). 

Installed Ansible by following [these](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#latest-releases-via-apt-ubuntu) instructions:

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

To find which Raspberry Pi is online, a python script parses the output of
`arp-scan`. The result is returned in json. 


### Ansible playbook development


### Run Ansible
`ansible-playbook -i inventory poll.yml` to find hosts online



