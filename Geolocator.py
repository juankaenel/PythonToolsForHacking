#!/usr/bin/python3

import os
import sys
import requests
import argparse
import json

"""
A simple tool to obtain geolocation via ipstack

Api_key: https://ipstack.com/signup/free

~ R4z0r
"""
    
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--ip', help="set IP")
parser.add_argument('-a', '--apiKey', help="set apiKey")
parser = parser.parse_args()

ip = parser.ip
api_key = parser.apiKey
url=f"http://api.ipstack.com/{ip}?access_key={api_key}"

if ip is None or api_key is None:
    print('\n[*] Use python3 ' + sys.argv[0] + '-i ip-address -a api_key')
    sys.exit(1)

def getLocation():
    response = requests.post(url=url, verify=False).json()
    
    ip = response["ip"]
    country_name = response["country_name"]
    continent_name = response["continent_name"]
    region_name = response["region_name"]
    city = response["city"]
    latitude = response["latitude"]
    longitude = response["longitude"]
    
    print('\n----------- Results -------------')
    print(f"\nIP: {ip} \nContinent Name: {continent_name} \nCountry Name: {country_name} \nRegion Name: {region_name} \nCity: {city} \nLatitude: {latitude} \nLongitude: {longitude}")
    print(f'\nIf you need to google maps the location you can use this link: https://www.google.com/maps/@{latitude},{longitude}')
 
if __name__ == "__main__":
    try:
        getLocation()
    except KeyboardInterrupt:
        print('[*] Exiting the program... thanks for use this tool.\n')
        sys.exit(0)