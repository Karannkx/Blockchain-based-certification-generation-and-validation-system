import requests
import os
from dotenv import load_dotenv
import pprint

# Load environment variables
load_dotenv()

def retrieve_from_pinata(jwt_token):
    url = "https://api.pinata.cloud/data/pinList"
    headers = {'Authorization': f'Bearer {jwt_token}'}

    response = requests.get(url, headers=headers)

    return response.json()

PINATA_JWT_TOKEN = os.getenv('PINATA_JWT_TOKEN')

pprint.pprint(retrieve_from_pinata(PINATA_JWT_TOKEN))
