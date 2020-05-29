# BasicNetmikoRouterConfigScript
This scripts adds a new loopback interface to a Cisco IOS router

Here are the router and computer configurations used for this script

## Bringing Router back to default configuration 
* Router> enable
* Router# write erase
* Router# Reload

## Set up an IP interface on Router
* Router> en
* Router# conf t
* Router(config)# int fa0/1
* Router(config-if)# ip address 192.168.99.1 255.255.255.0
* Router(config-if)# no shut
* Router(config-if)# exit


## Set up SSH on Router
* Router(config)# hostname CiscoRouter1841
* CiscoRouter1841(config)# ip domain-name jessebaldwin.net
* CiscoRouter1841(config)# crypto key generate rsa
* CiscoRouter1841(config)# ip ssh version 2
* CiscoRouter1841(config)# line vty 0 4
* CiscoRouter1841(config-line)# transport input ssh
* CiscoRouter1841(config-line)# login local
* CiscoRouter1841(config-line)# exit
* CiscoRouter1841(config)# username admin password password
* CiscoRouter1841(config)# enable secret secret

## Set up computer
* Set router facing interface to 192.168.99.100 255.255.255.0
* Install Python 3
* Install Netmiko
