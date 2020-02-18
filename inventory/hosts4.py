#!/usr/bin/python3

"""
	Find selected raspberry pi's 
	- Freshly flashed or
	- Already set as node in the cluster
	- Basically just a wrapper for arp-scan
	
		
	Output:
	- yaml style, for Ansible's hosts file
	
"""

import yaml
import subprocess


# Load mac / pi mapping
with open("group_vars/vars.yml", 'r') as stream:
    try:
        mac_mapping = yaml.load(stream)
        # print(yaml.dump(iets, default_flow_style=False))    #DEBUG
        raspis = mac_mapping["mac_address_mapping"]
    except yaml.YAMLError as exc:
        print(exc)
        exit(1)


# Perform an arp-scan, find hosts on the local network
arp_args = ('sudo', 'arp-scan', '-lq')
arp_scan = subprocess.check_output(arp_args)
hosts = arp_scan.decode("utf-8")
local_site = [i.split('\t') for i in hosts.split('\n') if 
    len(i) and i.startswith('192.') ]


# Start with compiling the output
# defaultdevices: "fresh" raspberry pi's, with dhcp ip address and 
#                  default login credentials
# nodes: already set-up devices, with static ip's equal to setting
#    node-master: 192.168.178.200 
#    nodes-clients: all others
defaultdevices = []
defaultdevices_vars = { "ansible_ssh_user": "pi",
                        "ansible_ssh_pass": "raspberry",
                        }

node_master = []
node_vars = { "ansible_ssh_user": "pi" }

nodes_clients = []


# Loop over each found host in local_site
for item in local_site:
    try:
        host = raspis[item[1].upper()]
        # print("Raspi found: {} - {} - {}".format(host["name"], host["ip"], item[1]))
        if host["ip"] == item[0]:
            # Configured device, check for master first, else client
            if host["ip"] == '192.168.1.200':
                node_master.append(host["ip"])
            else:
                nodes_clients.append(host["ip"])
        else:
            defaultdevices.append(item[0])
    except KeyError:
        # print("Host not found in mac_address_mapping {}".format(item))
        pass


# Build final dict for output        
inventory = { 
    "defaultdevices": { 
        "hosts": defaultdevices,
        "vars": defaultdevices_vars 
        },
    "node_master": { 
       "hosts": node_master,
       "vars": node_vars 
        },
    "node_clients": {
        "hosts": nodes_clients,
        "vars": node_vars 
        }
    }                   

# Print yaml, to be used as input for ansible-playbook                           
print(yaml.dump(inventory))




