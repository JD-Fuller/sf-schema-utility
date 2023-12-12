# Create a Python script, e.g., encrypt_credentials.py, and add the following code:

from credentials_manager import save_credentials

# Sample credentials to be encrypted
sample_credentials = {
    "username": "jdfuller@resilient-bear-szm4m.com",
    "password": "Thisistheway1",
    "security_token": "HuNkFTchD9rJ4891R36zLP4Je",
    "base_path": "https://login.salesforce.com"
}

# Encrypt and save the credentials
save_credentials(sample_credentials)

print("Credentials encrypted and saved successfully.")
