import os
import json
from dotenv import load_dotenv
from synarkos_client import SynarkOSClient

load_dotenv()

client = SynarkOSClient(api_key=os.getenv("SYNARKOS_API_KEY"))

print(json.dumps(client.models.list_available(), indent=4))
print(json.dumps(client.health.check(), indent=4))
print(json.dumps(client.synarkos.get_logs(), indent=4))
print(json.dumps(client.client.rate.get_limits(), indent=4))
print(json.dumps(client.synarkos.check_available(), indent=4))
