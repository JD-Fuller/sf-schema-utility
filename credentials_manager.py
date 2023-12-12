import json
import os
from crypto_utils import CryptoUtils

def encrypt_data(data):
    """
    Encrypt data.
    Args:
        data (str): Data to be encrypted.
    Returns:
        str: Encrypted data.
    """
    crypto_utils = CryptoUtils()
    try:
        return crypto_utils.encrypt_data(data)
    except Exception as e:
        print("Error encrypting data:", e)
        return None

def decrypt_data(encrypted_data):
    """
    Decrypt data.
    Args:
        encrypted_data (str): Data to be decrypted.
    Returns:
        str: Decrypted data.
    """
    crypto_utils = CryptoUtils()
    try:
        return crypto_utils.decrypt_data(encrypted_data)
    except Exception as e:
        print("Error decrypting data:", e)
        return None

# Example usage for general-purpose encryption/decryption
if __name__ == "__main__":
    sample_data = "Example data to encrypt"
    encrypted = encrypt_data(sample_data)
    if encrypted:
        print("Encrypted Data:", encrypted)
        decrypted = decrypt_data(encrypted)
        if decrypted:
            print("Decrypted Data:", decrypted)
