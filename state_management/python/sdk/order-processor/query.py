from time import sleep
import logging
from dapr.clients import DaprClient
import json

logging.basicConfig(level=logging.INFO)

DAPR_STORE_NAME = "statestore"

with DaprClient() as client:

    query = json.dumps({
        "filter": {
            "OR": [
                {"EQ": { "orderId": "1" }},
                {"IN": { "orderId": ["2", "3", "4"] }}
            ]
        }
    })

    # query = open('query.json', 'r').read()
    logging.info(query)

    query_resp = client.query_state(
        store_name=DAPR_STORE_NAME,
        query=query,
        states_metadata={"contentType": "application/json"},
    )

    for r in query_resp.results:
        print(r.key, json.dumps(json.loads(str(r.value, 'UTF-8')), sort_keys=True))
