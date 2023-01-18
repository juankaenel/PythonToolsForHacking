import requests
from bs4 import BeautifulSoup

url = 'https://lorem2.com/'
response = requests.get(url) # devuelve la respuesta en bytes, para pasarlo a texto usamos .text
soup = BeautifulSoup(response.text, 'html.parser')

for link in soup.find_all('a'):
    if link.get('href') != None:
        print(link.get('href'))
    else:
        pass