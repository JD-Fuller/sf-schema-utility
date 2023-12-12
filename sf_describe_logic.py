# sf_describe_logic.py

import logging
from simple_salesforce import Salesforce

def get_available_objects(token_data):
    try:
        sf = Salesforce(instance_url=token_data['instance_url'],
                        session_id=token_data['access_token'])
        return sf.describe()
    except Exception as e:
        logging.error(f"Error retrieving object list: {e}")
        return None

def describe_object(sObjectName, token_data):
    try:
        sf = Salesforce(instance_url=token_data['instance_url'],
                        session_id=token_data['access_token'])
        return sf.sobjects[sObjectName].describe()
    except Exception as e:
        logging.error(f"Error describing {sObjectName}: {e}")
        return None
