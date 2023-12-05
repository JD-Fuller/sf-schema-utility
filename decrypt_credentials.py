# Create another Python script, e.g., decrypt_credentials.py, and add the following code:

from credentials_manager import get_credentials

# Retrieve and decrypt the credentials
retrieved_credentials = get_credentials()

# Display the decrypted credentials
if retrieved_credentials:
    print("Decrypted Credentials:", retrieved_credentials)
else:
    print("Failed to retrieve or decrypt credentials.")
