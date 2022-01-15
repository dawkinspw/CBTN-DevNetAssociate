import requests
import json
from pprint import pprint

url = "https://sandbox-nxos-1.cisco.com/api/aaaLogin.json"

payload = json.dumps({
  "aaaUser": {
    "attributes": {
      "name": "admin",
      "pwd": "Admin_1234!"
    }
  }
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic YWRtaW46QWRtaW5fMTIzNCE=',
  'Cookie': 'APIC-cookie=e444ipG+fdMfPH3MmLspkRw9Vz+sHJGpw78ZxPNOYQM8Mz9vZzT9+0vmHI7mNb0CtOMrqdpTMj5KjCWixwSDkKf10I5Fu5AbzxO1OsE7LZHv5egWV1d4oVTCzra+E25O2om6InRNxGCdBa/DJ6BPyvfDgqX5hA0mkUx8zPyUCrg='
}

response = requests.post(url, headers=headers, data=payload, verify=False).json()

# pprint(response)
token = response['imdata'][0]['aaaLogin']['attributes']['token']
pprint(token)
cookies={}
cookies['APIC-cookie']=token