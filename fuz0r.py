#/usr/bin/python3
import warnings
import requests
import argparse

"""
Simple script para hacer fuzzing sobre un dominio
"""

parser = argparse.ArgumentParser()
parser.add_argument('-t','--target',help="set target")
parser.add_argument('-w','--wordlist',type=argparse.FileType('r'),help="set dictionary")
parser = parser.parse_args()

if parser.target:
    #with open(parser.wordlist, 'r') as f:
    print('\n------ Lanzando Fuzzer ------\n')
    for line in parser.wordlist:
        route = line.strip()
        response = requests.get(f'https://{parser.target}/{route}')
        print(f'https://{parser.target}/{route}: {response.status_code}')
else:
    f'[!] Uso: python3' + sys.argv[0] + '-t domain.com'
    