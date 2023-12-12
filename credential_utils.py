# credential_utils.py

import getpass

def prompt_for_credentials():
    print("Credentials not found in config.json. Please enter them manually.")
    username = input("Enter Salesforce username: ")
    password = getpass.getpass("Enter Salesforce password: ")
    security_token = getpass.getpass("Enter Salesforce security token: ")
    return {
        "username": username,
        "password": password,
        "security_token": security_token
    }

# Add more credential-related functions as needed
