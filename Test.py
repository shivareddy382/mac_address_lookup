import requests
import json
import os

def get_mac_lookup():
        mac_address = os.environ['macaddress']
        print("You entered: " + mac_address)
       #print('https://api.macaddress.io/v1?apiKey=at_vPxEIQqhTXID0OPufpq1KdoZkjLNL&output=json&search={}'.format(mac_address))
        response = requests.get('https://api.macaddress.io/v1?apiKey=at_vPxEIQqhTXID0OPufpq1KdoZkjLNL&output=json&search={}'.format(mac_address))
        print("Company Name: " + response.json()['vendorDetails']['companyName'])
        
get_mac_lookup()
