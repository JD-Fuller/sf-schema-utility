import json
import os
import logging
from sf_authentication import AuthConfig, SfAuth

# Function to load credentials from config.json
def load_credentials(environment):
    with open('config.json') as config_file:
        config = json.load(config_file)
        return config['client'][environment]

# Logging configuration
logging.basicConfig(level=logging.INFO)

def authenticate_using_username_password(environment):
    creds = load_credentials(environment)

    if not all([creds.get('username'), creds.get('password'), creds.get('security_token')]):
        logging.error("Error: Missing required credentials.")
        return None

    auth_config = AuthConfig(
        username=creds.get('username'),
        password=creds.get('password'),
        security_token=creds.get('security_token'),
        base_path=creds.get('base_path', 'https://login.salesforce.com')
    )

    sf_auth = SfAuth()
    try:
        return sf_auth.get_session_id_conn_app(auth_config)
    except Exception as e:
        logging.error(f"Authentication failed: {e}")
        return None
