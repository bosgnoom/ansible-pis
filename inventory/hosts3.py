#!/usr/bin/python3

"""
	Find selected raspberry pi's 
	- Freshly flashed or
	- Already set as node in the cluster system
	
	Output:
	- json style, for Ansible's hosts file
	
"""

import yaml
import subprocess

# Load mac / pi mapping
with open("group_vars/vars.yml", 'r') as stream:
    try:
        mac_mapping = yaml.load(stream)
        # print(yaml.dump(iets, default_flow_style=False))
        raspis = mac_mapping["mac_address_mapping"]
    except yaml.YAMLError as exc:
        print(exc)

# Perform an arp-scan, find hosts on the local network
arp_args = ('sudo', 'arp-scan', '-lq')
arp_scan = subprocess.check_output(arp_args)
hosts = arp_scan.decode("utf-8")
local_site = [i.split('\t') for i in hosts.split('\n') if 
    len(i) and i.startswith('192.') ]

# Start with compiling the output json format
# defaultdevices: "fresh" raspberry pi's, with dhcp ip address and 
#                  default login credentials
# nodes: already set-up devices, with static ip's equal to setting
defaultdevices_hosts = []
defaultdevices_vars = { "ansible_ssh_user": "pi",
                        "ansible_ssh_pass": "raspberry",
                        }

nodes_hosts = []
nodes_vars = { "ansible_ssh_user": "pi" }

# Loop over each found host in local_site
for item in local_site:
    try:
        host = raspis[item[1].upper()]
        #print("Raspi found: {} - {} - {}".format(host["name"], host["ip"], item[1]))
        if host["ip"] == item[0]:
            # print("IP adres al ingesteld")
            nodes_hosts.append(host["ip"])
        else:
            # print("IP adres nog niet ingesteld")
            defaultdevices_hosts.append(item[0])
    except KeyError:
        # print("Niet gevonden: {}".format(item))
        pass

# Build final json for output        
defaultdevices = { "hosts": defaultdevices_hosts,
                   "vars": defaultdevices_vars
                   }
nodes = { "hosts": nodes_hosts,
          "vars": nodes_vars
                   }
                   
inventory = { "defaultdevices": defaultdevices,
              "nodes": nodes
              }                   

# Print json, to be used as input for ansible-playbook                           
print(inventory)



    






