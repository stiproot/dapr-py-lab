from time import sleep
import logging
from dapr.clients import DaprClient
import json

logging.basicConfig(level=logging.INFO)

DAPR_STORE_NAME = "statestore"

with DaprClient() as client:
    # for i in range(1, 10):
        # orderId = str(i)
        # order = {"orderId": orderId}
        # document = json.dumps(order)

        # client.save_state(DAPR_STORE_NAME, orderId, document, metadata={"contentType": "application/json"})
        # logging.info('Saving Order: %s', document)

        # result = client.get_state(DAPR_STORE_NAME, orderId)
        # logging.info('Result after get: ' + str(result.data))

        # "sort": [
        #     {
        #         "key": "orderId",
        #         "order": "DESC"
        #     }
        # ]

        # Delete state from the state store
        # client.delete_state(store_name=DAPR_STORE_NAME, key=orderId)
        # logging.info('Deleting Order: %s', order)
        # sleep(1)

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

    # logging.info(query_resp.results)

    for r in query_resp.results:
        print(r.key, json.dumps(json.loads(str(r.value, 'UTF-8')), sort_keys=True))
