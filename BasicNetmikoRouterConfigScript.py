#!/usr/bin/env python

# Importing the ConectionHandeler from the Netmiko library
from netmiko import ConnectHandler

# Conection details for the Cisco Router
cisco_1841 = {
    'device_type': 'cisco_ios',
    'host':   '192.168.99.1',
    'username': 'admin',
    'password': 'password',
    'port' : 22,
    'secret': 'secret',
}

# Open SSH session
CiscoRouter1841 = ConnectHandler(**cisco_1841)

# Get the IP Interface Breif
print(CiscoRouter1841.send_command('show ip int brief'))

# Enter enable mode, uses the eable sectret Key
CiscoRouter1841.enable()

# Configure Loopback
config_commands = [ 'interface lo3',
                    'ip address 3.3.3.3 255.255.255.255',
                    'no shut' ]
print(CiscoRouter1841.send_config_set(config_commands))

# Get the IP Interface Breif to see the new loopback interface
print(CiscoRouter1841.send_command('show ip int brief'))

# close SSH connection
CiscoRouter1841.disconnect()