import requests
import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()

# Retrieve environment variables
EVE_NG_HOST = os.getenv("EVE_NG_HOST")
EVE_NG_USERNAME = os.getenv("EVE_NG_USERNAME")
EVE_NG_PASSWORD = os.getenv("EVE_NG_PASSWORD")

# Define the login endpoint URL
LOGIN_ENDPOINT = f"http://{EVE_NG_HOST}/api/auth/login"

# Define the payload for the login request
payload = {
    "username": EVE_NG_USERNAME,
    "password": EVE_NG_PASSWORD
}

# Send a POST request to the login endpoint
response = requests.post(LOGIN_ENDPOINT, json=payload)

# Check if the request was successful
if response.status_code == 200:
    print("Login successful!")
    print("Response:", response.json())
else:
    print("Login failed. Status code:", response.status_code)
    print("Response:", response.text)
