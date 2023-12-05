from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
import os

class CryptoUtils:
    def __init__(self):
        # Generate or load an RSA key pair (private and public keys)
        self.private_key, self.public_key = self.generate_rsa_key_pair()

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
        encrypted = self.public_key.encrypt(
            data.encode(),
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return encrypted

    def decrypt_data(self, encrypted_data):
        # Decrypt data using the private key
        decrypted = self.private_key.decrypt(
            encrypted_data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return decrypted.decode()

# Example usage
if __name__ == "__main__":
    crypto_utils = CryptoUtils()
    original_data = "Sensitive Information"
    encrypted_data = crypto_utils.encrypt_data(original_data)
    decrypted_data = crypto_utils.decrypt_data(encrypted_data)

    print("Original:", original_data)
    print("Encrypted:", encrypted_data)
    print("Decrypted:", decrypted_data)
