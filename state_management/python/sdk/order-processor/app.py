from time import sleep
import logging
from dapr.clients import DaprClient
import json

logging.basicConfig(level=logging.INFO)

DAPR_STORE_NAME = "statestore"

with DaprClient() as client:
    for i in range(1, 10):
        orderId = str(i)
        order = {"orderId": orderId}
        document = json.dumps(order)

        client.save_state(DAPR_STORE_NAME, orderId, document, metadata={"contentType": "application/json"})
        logging.info('Saving Order: %s', document)

        result = client.get_state(DAPR_STORE_NAME, orderId)
        logging.info('Result after get: ' + str(result.data))

        client.delete_state(store_name=DAPR_STORE_NAME, key=orderId)
        logging.info('Deleting Order: %s', order)
        sleep(1)
