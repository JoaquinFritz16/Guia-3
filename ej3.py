import requests
import pyperclip
from bs4 import BeautifulSoup
def save_html():
    soup = BeautifulSoup(response.text, 'html.parser')
    articulos = soup.find_all('a')
    for a in articulos:
        enlace = a.get("href")
        if enlace.lower().startswith("https://chequeado.com/blog/?current-page"):
            lista.append(enlace)
    print(lista)

lista=[]    
while True:
    try:
        url = pyperclip.paste()
        print(url)
        response = requests.get(url)
        print(response)
        response.raise_for_status()
        save_html()
        break
    except requests.exceptions.RequestException as e:
        print('Flaco elegi una url de una pagina: ', e)
        break
