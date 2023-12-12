# sf_describe_logic.py

import logging
from sf_authentication import authenticate_to_salesforce

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
