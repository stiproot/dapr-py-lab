import requests
import json

url = "http://localhost:3500/v1.0/state/statestore/query"

# payload = "@query-api-examples/dataset.json"
payload = {
    "filter": {
        "EQ": { "orderId": "1" }
    },
    "sort": [
        {
            "key": "orderId",
            "order": "DESC"
        }
    ]
}

headers = {
  'Content-Type': 'application/json',
  'dapr-app-id': 'demo',
}

response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

print(response.text)
