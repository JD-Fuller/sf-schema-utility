from simple_salesforce import Salesforce
from credentials_manager import get_credentials

def authenticate_to_salesforce():
    creds = get_credentials()

    if creds:
        try:
            sf = Salesforce(
                username=creds['username'],
                password=creds['password'],
                security_token=creds['security_token']
            )
            print("Authenticated to Salesforce")
            # Use `sf` to perform operations
        except Exception as e:
            print(f"Authentication failed: {e}")
    else:
        print("Error: Unable to retrieve or decrypt credentials.")

if __name__ == '__main__':
    authenticate_to_salesforce()
