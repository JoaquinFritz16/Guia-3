import requests
import pyperclip
from bs4 import BeautifulSoup
from selenium import webdriver

def save_html(response):
    soup = BeautifulSoup(response.text, 'html.parser')
    articulos = soup.find_all('a')
    for a in articulos:
        enlace = a.get("href")
        if enlace and 'pagination' in enlace:
            lista.append(enlace)
    print(lista)

lista = []    

while True:
    try:
        url = pyperclip.paste()
        response = requests.get(url)
        response.raise_for_status()
        save_html(response)
        break
    except requests.exceptions.RequestException as e:
        print('Por favor, elige una URL válida: ', e)
        break
