import requests
import json

# Credential Checeknig 
import os
from dotenv import load_dotenv
import requests

# Load environment variables from .env file
load_dotenv()

# Get environment variables
EVE_NG_HOST = os.getenv("EVE_NG_HOST")
EVE_NG_USERNAME = os.getenv("EVE_NG_USERNAME")
EVE_NG_PASSWORD = os.getenv("EVE_NG_PASSWORD")

# Check if EVE_NG_HOST is defined
if EVE_NG_HOST is None:
    raise ValueError("EVE_NG_HOST environment variable is not defined")



# Lab configuration
LAB_NAME = "my_lab"
LAB_NODES = [
    {
        "name": "router1",
        "type": "qemu",
        "image": "ios-15.2",
        "config": "config1.txt"
    },
    {
        "name": "switch1",
        "type": "qemu",
        "image": "nxos-9.2",
        "config": "config2.txt"
    },
    {
        "name": "pc1",
        "type": "qemu",
        "image": "ubuntu-20.04",
        "config": "config3.txt"
    }
]

# API endpoints
LOGIN_ENDPOINT = f"https://{EVE_NG_HOST}/api/auth/login"
LAB_ENDPOINT = f"https://{EVE_NG_HOST}/api/labs"

# Login to EVE-ng
login_data = {
    "username": EVE_NG_USERNAME,
    "password": EVE_NG_PASSWORD
}
response = requests.post(LOGIN_ENDPOINT, json=login_data, verify=False)
if response.status_code == 200:
    token = response.json()["token"]
else:
    print(f"Login failed: {response.status_code} - {response.text}")
    exit(1)

# Create the lab
lab_data = {
    "name": LAB_NAME,
    "nodes": LAB_NODES
}
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}
response = requests.post(LAB_ENDPOINT, headers=headers, json=lab_data, verify=False)
if response.status_code == 200:
    print(f"Lab '{LAB_NAME}' created successfully.")
else:
    print(f"Lab creation failed: {response.status_code} - {response.text}")
    exit(1)