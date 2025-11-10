from synarkos_client import SynarkOSClient
from dotenv import load_dotenv
import os

load_dotenv()

client = SynarkOSClient(api_key=os.getenv("SYNARKOS_API_KEY"))

response = client.client.rate.get_limits()
print(response)

print(client.health.check())
