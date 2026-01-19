import os
import requests
from dotenv import load_dotenv

load_dotenv()

def check_token_scopes():
    token = os.environ.get('ACCESS_TOKEN')
    if not token:
        raise ValueError("ACCESS_TOKEN environment variable is not set")

    headers = {
        'Authorization': f'token {token}'
    }
    response = requests.get('https://api.github.com/user', headers=headers)
    
    if response.status_code == 200:
        scopes = response.headers.get('X-OAuth-Scopes')
        print(f"Token scopes: {scopes}")
    else:
        print(f"Failed to check token scopes: {response.status_code} {response.text}")

if __name__ == "__main__":
    check_token_scopes()