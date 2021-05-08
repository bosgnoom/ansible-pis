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

### Git to remember
- `git status`: Shows which files are changed/untracked
- `git add .`: Will add all untracked files
- `git commit -a -m <message>`: Commit changes
- `git push`: "Save" repository to remote server(s)
- `git init`: Make a git repository in the currect directory


## Ansible
Ansible will be used for:
- [x] Set up the raspberry pi:
  - Install packages often used by me:
    - mc
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
- [?] Set up the OLED display:
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
- [?] Prepare for kubernetes:
  - cgroup
  - disable swap

TODO:
- [ ] Set up private registry
  - [ ] Registry


### Install Ansible
Installed Ansible by following [these](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#latest-releases-via-apt-ubuntu) instructions:

```
$ sudo apt update
$ sudo apt install software-properties-common
$ sudo apt-add-repository --yes --update ppa:ansible/ansible
$ sudo apt install ansible
```


### Ansible inventory
As default, Ansible uses `/etc/ansible` for configuring the hosts/nodes. As I
want to learn Ansible without running with root permissions, I have developed a
playbook which determines the hosts by their mac address. Running `nmap -sP` fills
the arp table, which can be used by an user to lookup mac address to ip address. 


### Run Ansible
Run Ansible by: `ansible-playbook playbook.yml`. Different playbooks
are developed:
- site.yml: main playbook. Will convert a new device to either master or node.
- shutdown.yml: shuts all nodes down


## TODO
- [ ] Develop a python3 script to show node info on OLED
  - Like... ip address, cpu usage, mem stat, ...
  - Start with "stats.py" on boot...
- [x] Start with installing kubernetes
  - At the moment Rancher's k3s is my first to test
  - Check [this out](https://github.com/rancher/k3s)
- [ ] Add nmap for install on localhost, as it is needed...

When setting up new devices:
- Ansible needs ```export ANSIBLE_HOST_KEY_CHECKING=False```

