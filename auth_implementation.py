from sf_authentication import AuthConfig, SfAuth
from credentials_manager import get_credentials

def authenticate_using_username_password():
    # Retrieve encrypted credentials
    creds = get_credentials()

    if creds:
        # Extract credentials
        username = creds.get('username')
        password = creds.get('password')
        security_token = creds.get('security_token')
        client_id = creds.get('client_id')  # Only needed for connected app auth
        client_secret = creds.get('client_secret')  # Only needed for connected app auth
        base_path = creds.get('base_path', 'https://login.salesforce.com')  # Default to standard login URL

        if not all([username, password, security_token, client_id, client_secret]):
            print("Error: Missing required credentials.")
            return

        # Create a configuration object
        config = AuthConfig(client_id, client_secret, username, password, security_token, base_path)

        # Create an authentication object
        sf_auth = SfAuth()

        # Get session ID using username and password
        try:
            session_id = sf_auth.get_session_id_un_pw(config)
            print(f"Session ID: {session_id}")
        except Exception as e:
            print(f"Authentication failed: {e}")

        # Uncomment the following lines if you want to authenticate using a connected app
        # try:
        #     session_info = sf_auth.get_session_id_conn_app(config)
        #     print(f"Session Info: {session_info}")
        # except Exception as e:
        #     print(f"Connected App Authentication failed: {e}")

    else:
        print("Error: Unable to retrieve or decrypt credentials.")

if __name__ == '__main__':
    authenticate_using_username_password()
