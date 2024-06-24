import requests
import json

URL = "http://127.0.0.1:8000/stucreate/"

data = {
    "name": "Sohan",
    "roll": 101, 
    "city": "Noida",
}
headers = {'Content-Type': 'application/json'}
json_data = json.dumps(data)
r = requests.post(url=URL, data=json_data, headers=headers)
try:
    data = r.json()
    print(data)
except ValueError:
    print("Response is not in JSON format", r.text)
