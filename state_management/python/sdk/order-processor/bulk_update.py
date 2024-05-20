import json
from dapr.clients import DaprClient
from dapr.clients.grpc._state import StateItem

# json_file_path = 'dataset.json'
# with open(json_file_path, 'r') as file:
#     data = json.load(file)

data = [{"key": str(d), "value": json.dumps({"orderId": str(d)})} for d in range(1, 10)]

with DaprClient() as client:
    state_entries = []
    for item in data:
        state_entries.append(StateItem(key=item['key'], value=item['value'], metadata={"contentType": "application/json"}))
    
    client.save_bulk_state(store_name='statestore', states=state_entries)

    print("State persisted successfully.")