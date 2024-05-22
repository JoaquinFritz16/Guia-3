import requests
import pyperclip
from bs4 import BeautifulSoup
import os


def url_valida(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return True
    except requests.exceptions.RequestException:
        return False
def obtener_calificaciones(url):
    response=requests.get(url)
    sopa=BeautifulSoup(response.text, 'html.parser')
    calificaciones=sopa.find_all('p', { 'class="ui-review-capability__rating__average ui-review-capability__rating__average--desktop">4.5</p>'})
    print(calificaciones)
url = pyperclip.paste()
print(url)
while True:
    if url_valida():
        nombre_producto=input('Ingrese el nombre del producto: ')
    else:
        print('URL no valida')
    break