import json
import os
from crypto_utils import CryptoUtils  # Ensure this uses AES encryption

def save_credentials(credentials):
    """
    Encrypt and save credentials to a file.
    Args:
        credentials (dict): A dictionary containing credentials.
    """
    crypto_utils = CryptoUtils()
    try:
        encrypted_credentials = crypto_utils.encrypt_data(json.dumps(credentials))
        with open('.credentials.json', 'w') as file:  # Note the change to 'w'
            file.write(encrypted_credentials)
    except Exception as e:
        print("Error saving credentials:", e)

def get_credentials():
    """
    Retrieve and decrypt credentials from a file.
    Returns:
        dict: A dictionary of decrypted credentials.
    """
    crypto_utils = CryptoUtils()
    try:
        with open('.credentials.json', 'r') as file:  # Note the change to 'r'
            encrypted_credentials = file.read()
            decrypted_credentials = crypto_utils.decrypt_data(encrypted_credentials)
            return json.loads(decrypted_credentials) if decrypted_credentials else None
    except Exception as e:
        print("Error retrieving credentials:", e)
        return None

# Example usage
if __name__ == "__main__":
    creds = {
        "username": "jdfuller@resilient-bear-szma4m.com",
        "password": "Thisistheway1",
        "security_token": "HuNkFTchD9rJ4891R36zLP4Je",
        "base_path": "https://login.salesforce.com"
    }
    save_credentials(creds)

    retrieved_creds = get_credentials()
    if retrieved_creds:
        print("Retrieved Credentials:", retrieved_creds)
    else:
        print("Failed to retrieve credentials.")
