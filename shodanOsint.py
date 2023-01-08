#!/usr/bin/python3

import requests

"""Este script solicita al usuario que ingrese una consulta de Shodan y luego utiliza la librería "requests" de Python para enviar una solicitud a la API de Shodan. La respuesta de la API se almacena en la variable "response", que se pasa a un diccionario Python utilizando la función "response.json()". Luego, se recorren los resultados de la búsqueda (almacenados en la clave "matches" del diccionario) y se imprime la ciudad para cada host (almacenada en la clave "location" del diccionario)."""

API_KEY = "YOUR_API_KEY_HERE"

query = input("Ingresa tu consulta de Shodan: ")
url = f"https://api.shodan.io/shodan/host/search?key={API_KEY}&query={query}"
response = requests.get(url) # return dict  total, matches
    
try:
    for host in response.json()['matches']:
        print(f"Dirección ip: {host['ip_str']}")
        print(f"Puerto: {host['port']}")
        print(f"Organización: {host['org']}")
        print(f"City: {host['location']['city']}")
        print(f"Data: {host['data']}\n")
except:
    print("Error en la consulta")
