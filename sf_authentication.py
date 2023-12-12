import json
import logging
from simple_salesforce import Salesforce

# Function to load credentials from config.json
def load_credentials(environment):
    with open('config.json') as config_file:
        config = json.load(config_file)
        return config['client'][environment]

# Logging configuration
logging.basicConfig(level=logging.INFO)

def authenticate_to_salesforce(environment):
    creds = load_credentials(environment)

    if not all([creds.get('username'), creds.get('password'), creds.get('security_token')]):
        logging.error("Error: Missing required Salesforce credentials.")
        return None

    try:
        sf = Salesforce(
            username=creds['username'],
            password=creds['password'],
            security_token=creds['security_token']
        )
        return sf
    except Exception as e:
        logging.error(f"Salesforce authentication failed: {e}")
        return None

# Example usage
if __name__ == "__main__":
    environment = 'dev'  # or 'qa_uat', 'prod'
    sf = authenticate_to_salesforce(environment)
    if sf:
        print("Authenticated to Salesforce")
        # Proceed with Salesforce operations using the 'sf' object
    else:
        print("Authentication failed.")
