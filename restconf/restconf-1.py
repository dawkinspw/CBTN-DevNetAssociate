import requests

url = "https://sandbox-iosxe-latest-1.cisco.com/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface=GigabitEthernet1"

payload={}
headers = {
  'Authorization': 'Basic ZGV2ZWxvcGVyOkMxc2NvMTIzNDU='
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
