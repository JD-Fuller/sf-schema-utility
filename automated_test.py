# Sample code for automated testing using unittest
import unittest
from crypto_utils import CryptoUtils

class TestEncryptionDecryption(unittest.TestCase):
    def test_encrypt_decrypt(self):
        # Simulate encryption and decryption
        credentials = {
            "username": "jdfuller@resilient-bear-szma4m.com",
            "password": "Thisistheway1",
            "security_token": "y5LGouo2qcquNLQWNoLOIYukC",
            "base_path": "https://login.salesforce.com"
        }

        crypto_utils = CryptoUtils()
        encrypted_data = crypto_utils.encrypt_data(credentials)
        decrypted_data = crypto_utils.decrypt_data(encrypted_data)

        # Assertion to validate decryption
        self.assertEqual(credentials, decrypted_data)

if __name__ == '__main__':
    unittest.main()
