from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography.exceptions import InvalidKey, InvalidSignature
import os

class CryptoUtils:
    def __init__(self):
        # Generate or load an RSA key pair (private and public keys)
        try:
            self.private_key, self.public_key = self.generate_rsa_key_pair()
        except Exception as e:
            print("Error generating RSA key pair:", e)
            self.private_key, self.public_key = None, None

    def generate_rsa_key_pair(self):
        # Generate a new RSA key pair
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        public_key = private_key.public_key()

        # Alternatively, load existing keys from a file or environment variable
        # private_key = serialization.load_pem_private_key(...)

        return private_key, public_key

    def encrypt_data(self, data):
        # Encrypt data using the public key
        try:
            encrypted = self.public_key.encrypt(
                data.encode(),
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            return encrypted
        except Exception as e:
            print("Encryption error:", e)
            return None

    def decrypt_data(self, encrypted_data):
        # Decrypt data using the private key
        try:
            decrypted = self.private_key.decrypt(
                encrypted_data,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None
                )
            )
            return decrypted.decode()
        except Exception as e:
            print("Decryption error:", e)
            return None

# Example usage
if __name__ == "__main__":
    crypto_utils = CryptoUtils()
    original_data = "Sensitive Information"
    encrypted_data = crypto_utils.encrypt_data(original_data)
    if encrypted_data:
        decrypted_data = crypto_utils.decrypt_data(encrypted_data)
        if decrypted_data:
            print("Original:", original_data)
            print("Encrypted:", encrypted_data)
            print("Decrypted:", decrypted_data)
        else:
            print("Decryption failed.")
    else:
        print("Encryption failed.")
