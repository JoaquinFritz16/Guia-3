import requests
import pyperclip
from bs4 import BeautifulSoup
lista=[]
def save_html():
    soup = BeautifulSoup(response.text, 'html.parser')
    parrafos = soup.find_all('p')
    for p in parrafos:
        texto=p.get_text()
        lista.append(texto)
        print(lista)
while True:
    try:
        url = pyperclip.paste()
        response = requests.get(url)
        response.raise_for_status()
        html = response.text
        save_html()
        break
    except requests.exceptions.RequestException as e:
        print('Flaco elegi una url de una pagina: ', e)

        break