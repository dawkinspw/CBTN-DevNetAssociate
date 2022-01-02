import requests
import json
from pprint import pprint

from requests.api import head

# set up connection parameters in a dict
router = {"ip": "sandbox-iosxe-latest-1.cisco.com", "port": "443",
            "user": "developer", "password": "C1sco12345"}

# set REST API headers
headers = {"Accept": "application/yang-data+json",
            "Content-Type": "application/yang-data+json"}

url = f"https://{router['ip']}/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface=GigabitEthernet1"

response = requests.get(url, headers=headers, auth=(
            router['user'], router['password']), verify=False)

api_data = response.json()

# print("/" * 50)
# pprint(api_data)
print("/" * 50)
pprint(api_data["Cisco-IOS-XE-interfaces-oper:interface"]["description"])
print("/" * 50)
if api_data["Cisco-IOS-XE-interfaces-oper:interface"]["admin-status"] =='if-state-up':
    print('Interface is up')