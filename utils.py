import json


def get_credentials():
    """Gets the credentials from local_config.json file"""
    cred_file = open('local_config.json')
    creds = json.load(cred_file)
    cred_file.close()
    return creds
