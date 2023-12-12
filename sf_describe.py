import argparse
import logging
from sf_authentication import authenticate_to_salesforce
import menu
import credential_utils  # Import the credential utility module

# Set up command-line argument parsing
parser = argparse.ArgumentParser(description='Describe Salesforce Object')
parser.add_argument('-e', '--env', default='dev', choices=['dev', 'qa_uat', 'prod'], help='Specify the environment (default: dev)')
parser.add_argument('-o', '--object', default='', help='Specify the Salesforce object to describe (default: lists all objects)')

# Logging configuration
logging.basicConfig(level=logging.INFO)

def get_available_objects(sf_instance):
    try:
        return sf_instance.describe()
    except Exception as e:
        logging.error(f"Error retrieving object list: {e}")
        return None

def describe_object(sObjectName, sf_instance):
    try:
        return sf_instance.sobjects[sObjectName].describe()
    except Exception as e:
        logging.error(f"Error describing {sObjectName}: {e}")
        return None

def main():
    menu.display_startup_menu()
    args = parser.parse_args()
    sf = authenticate_to_salesforce(args.env)

    if sf is None:
        creds = credential_utils.prompt_for_credentials()
        sf = authenticate_to_salesforce(args.env, creds)

    if sf is None:
        logging.error("Error: Salesforce authentication failed.")
        return

    if args.object:
        # Describe the specified Salesforce object
        describe_results = describe_object(args.object, sf)
        logging.info(f"Describe Results for {args.object}: {describe_results}")
    else:
        # List all available Salesforce objects
        available_objects = get_available_objects(sf)
        if available_objects:
            logging.info("Available Salesforce Objects:")
            for obj in available_objects['sobjects']:
                logging.info(f" - {obj['label']} ({obj['name']})")

if __name__ == '__main__':
    main()
