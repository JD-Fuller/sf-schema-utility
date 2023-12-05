import json
import os
from crypto_utils import CryptoUtils

def save_credentials(credentials):
    """
    Encrypt and save credentials to a file.

    Args:
        credentials (dict): A dictionary containing credentials.
    """
    crypto_utils = CryptoUtils()
    try:
        encrypted_credentials = crypto_utils.encrypt_data(json.dumps(credentials))
        with open('.credentials.json', 'wb') as file:
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
        with open('.credentials.json', 'rb') as file:
            encrypted_credentials = file.read()
            decrypted_credentials = crypto_utils.decrypt_data(encrypted_credentials)
            return json.loads(decrypted_credentials) if decrypted_credentials else None
    except Exception as e:
        print("Error retrieving credentials:", e)
        return None

# Example usage
if __name__ == "__main__":
    # Example credentials
    creds = {"username": "user", "password": "pass"}
    save_credentials(creds)

    retrieved_creds = get_credentials()
    if retrieved_creds:
        print("Retrieved Credentials:", retrieved_creds)
    else:
        print("Failed to retrieve credentials.")
