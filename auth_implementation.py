from sf_authentication import AuthConfig, SfAuth

def authenticate_using_username_password():
    # Configuration parameters for Salesforce authentication
    username = 'your_username'
    password = 'your_password'
    security_token = 'your_security_token'
    client_id = 'your_client_id'  # Only needed for connected app auth
    client_secret = 'your_client_secret'  # Only needed for connected app auth
    base_path = 'https://login.salesforce.com'  # May change for sandboxes or custom domains
    
    # Create a configuration object
    config = AuthConfig(client_id, client_secret, username, password, security_token, base_path)
    
    # Create an authentication object
    sf_auth = SfAuth()
    
    # Get session ID using username and password
    session_id = sf_auth.get_session_id_un_pw(config)
    print(f"Session ID: {session_id}")

    # Uncomment the following lines if you want to authenticate using a connected app
    # session_info = sf_auth.get_session_id_conn_app(config)
    # print(f"Session Info: {session_info}")

if __name__ == '__main__':
    authenticate_using_username_password()
