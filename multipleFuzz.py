#/usr/bin/python3
import argparse
import requests
import sys

"""
Simple script para hacer fuzzing, con la opción de setear varios targets

By: R4z0r
"""

parser = argparse.ArgumentParser()

# Creamos un grupo exclusivo para los argumentos target y multiple-targets
group = parser.add_mutually_exclusive_group()
group.add_argument('-t','--target', help="set target")
group.add_argument('-tf','--target_file', help="set target file", type=argparse.FileType('r'))
parser.add_argument('-w','--wordlist',type=argparse.FileType('r'),help="set dictionary")
parser = parser.parse_args()


# Si se ha proporcionado el argumento target, realizamos el fuzzing sobre una única URL
if parser.target:
    print(f'\n------ Lanzando Fuzzer para {parser.target} ------\n')
    for line in parser.wordlist:
        route = line.strip()
        try:
            response = requests.get(f'https://{parser.target}/{route}', timeout=4)
            print(f'https://{parser.target}/{route}: {response.status_code}')
        except requests.exceptions.ConnectTimeout:
            print("La petición ha excedido el tiempo de espera establecido")

# Si se ha proporcionado el argumento target_file, realizamos el fuzzing sobre varias URLs
elif parser.target_file:
    targets = parser.target_file.read().splitlines()
    for target in targets:
        print(f'\n------ Lanzando Fuzzer para {target} ------\n')
        for line in parser.wordlist:
            route = line.strip()
            try:
                response = requests.get(f'https://{target}/{route}',timeout=4)
                print(f'https://{target}/{route}: {response.status_code}')
            except requests.exceptions.ConnectTimeout:
                print("La petición ha excedido el tiempo de espera establecido")
        parser.wordlist.seek(0) # De esta forma después de cada iteración del ciclo for que recorre los targets, se posiciona el puntero del archivo al inicio y se puede volver a recorrer completamente en la siguiente iteración.
                
else:
   print("[!] Uso: python3 " + sys.argv[0] + " -f domain.com -w dict.txt | -tf urls.txt -w dict.txt")
    

    
