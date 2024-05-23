import requests
import pyperclip
from bs4 import BeautifulSoup
import os

def descargar_pdf(url, direc):
    try:
        response = requests.get(url)
        response.raise_for_status()
        nombre_archivo = os.path.basename(url)
        ruta_archivo = os.path.join(direc, nombre_archivo)
        with open(ruta_archivo, 'wb') as f:
            f.write(response.content)
        print(f"PDF descargado: {ruta_archivo}")
    except requests.exceptions.RequestException as e:
        print(f"No se pudo descargar el PDF: {e}")

lista=[]
url = pyperclip.paste()
    
response = requests.get(url)
response.raise_for_status()

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    directorio_pdf = 'pdfs'
    if not os.path.exists(directorio_pdf):
        os.makedirs(directorio_pdf)
    articulos = soup.find_all('a')
    for a in articulos:
        enlace = a.get('href')
    if enlace and enlace.lower().endswith('.pdf') and not enlace.startswith('blank:#'):
        descargar_pdf(enlace, directorio_pdf)
    lista.append(enlace)
    print(lista)

else:
    print(f"No se pudo acceder a la URL: {response.status_code}")
