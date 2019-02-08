#!/usr/bin/python3

"""
	Find selected raspberry pi's 
	- Freshly flashed or
	- Already set as node in the cluster system
	
	Output:
	- ini style, for Ansible's hosts file
	
"""

import yaml
import subprocess

# Load mac / pi mapping
with open("group_vars/vars.yml", 'r') as stream:
    try:
        iets = yaml.load(stream)
        # print(yaml.dump(iets, default_flow_style=False))
        raspis = iets["mac_address_mapping"]
    except yaml.YAMLError as exc:
        print(exc)

arp_args = ('sudo', 'arp-scan', '-lqx')
result = subprocess.check_output(arp_args)
text = result.decode("utf-8")

local_site = [aaa.split('\t') for aaa in text.split('\n') if len(aaa)]

nodes_hosts = []
nodes_vars = { "ansible_ssh_user": "pi" }
defaultdevices_hosts = []
defaultdevices_vars = { "ansible_ssh_user": "pi",
                        "ansible_ssh_pass": "raspberry",
                        }

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
        
defaultdevices = { "hosts": defaultdevices_hosts,
                   "vars": defaultdevices_vars
                   }
nodes = { "hosts": nodes_hosts,
          "vars": nodes_vars
                   }
                   
inventory = { "defaultdevices": defaultdevices,
              "nodes": nodes
              }                   
                           
print(inventory)



    






