# Sample code for manual testing
from crypto_utils import CryptoUtils

# Load encrypted data from .credentials.json
with open('.credentials.json', 'r') as file:
    encrypted_credentials = file.read()

# Decrypt the data
crypto_utils = CryptoUtils()
decrypted_credentials = crypto_utils.decrypt_data(encrypted_credentials)

# Print the decrypted credentials
print("Decrypted Credentials:", decrypted_credentials)
