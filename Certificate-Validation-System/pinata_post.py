import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def upload_to_pinata(file_path, jwt_token):
    url = "https://api.pinata.cloud/pinning/pinFileToIPFS"
    headers = {'Authorization': f'Bearer {jwt_token}'}

    with open(file_path, 'rb') as file:
        response = requests.post(url, files={'file': file}, headers=headers)
        return response.json()

# Load Pinata JWT Token from environment variable
PINATA_JWT_TOKEN = os.getenv('PINATA_JWT_TOKEN')

# Replace FILE_PATH with the path of the file you want to upload
FILE_PATH = 'certificate.pdf'

# Upload file to Pinata
result = upload_to_pinata(FILE_PATH, PINATA_JWT_TOKEN)

print(result)
