import requests
import config as cf

def getRequestData(api):
    # connect to the api and get the values
    r = requests.get(api, auth=(cf.alfresco_details['user'], cf.alfresco_details['pass']))
    return r.text
