import sys
import requests
import argparse

"""

Esta herramienta permite obtener los headers como Server o X-Powered-By que brindan información sobre las tecnologías de la aplicación.

~ R4z0r

"""



parser = argparse.ArgumentParser()
parser.add_argument('-t', '--target', help="set domain")
parser = parser.parse_args()

if parser.target:
    response = requests.get(parser.target)
    headers = response.headers

    if "Server" in headers or "server" in headers or "X-Powered-By" in headers:
        for header, value in headers.items():
            if header.lower() in ["server", "x-powered-by"]:
                print(f"Se han encontrado los encabezados {header}:{value}")
    else:
        print("Ninguno de los encabezados buscados se encontró en la respuesta.")

else:
    print("\n[!] Uso: python3 " + sys.argv[0] + " -t https://domain.com \n")
