import requests
import json
import os
from sf_authentication import SfAuth, AuthConfig
from credentials_manager import get_credentials

API_VERSION = '52.0'

def describe(sObjectName, api_version, token_data):
    base_path = token_data['instance_url']
    resource_path = '/services/data/v' + api_version + '/sobjects/'
    endpoint = base_path + resource_path + sObjectName + '/describe'
    headers = {
        'Authorization': token_data['token_type'] + ' ' + token_data['access_token']
    }

    resp = requests.get(endpoint, headers=headers)
    return resp.json()

def main():
    creds = get_credentials()
    if creds:
        auth_config = AuthConfig(
            client_id=creds.get('client_id'),
            client_secret=creds.get('client_secret'),
            username=creds.get('username'),
            password=creds.get('password'),
            security_token=creds.get('security_token'),
            base_path=creds.get('base_path', 'https://login.salesforce.com')
        )

        sf_auth = SfAuth()
        token_data = sf_auth.get_session_id_conn_app(auth_config)
        if 'access_token' in token_data:
            # Example: Describe a specific Salesforce object
            sObjectName = 'Account'  # Replace with the actual object name
            describe_results = describe(sObjectName, API_VERSION, token_data)
            # Process describe_results as needed
        else:
            print("Error: Salesforce authentication failed.")
    else:
        print("Error: Unable to retrieve or decrypt credentials.")

if __name__ == '__main__':
    main()
