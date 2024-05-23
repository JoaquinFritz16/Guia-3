import requests
import pyperclip
from bs4 import BeautifulSoup
import os
"""Utilizo esta pagina para comprobar el codigo: https://www.mercadolibre.com.ar"""
def obtener_calificaciones(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        calificaciones = soup.find_all('span', class_='ui-review-capability__rating__average')
        return calificaciones
    except requests.exceptions.RequestException as e:
        print('Error al obtener las calificaciones:', e)
        return None

def obtener_palabras_clave(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        comentarios = soup.find_all('div', class_='ui-review__content')
        palabras_claves = []
        for comentario in comentarios:
            palabras_claves.append(comentario.get_text().strip())
        return palabras_claves
    except requests.exceptions.RequestException as e:
        print('Error al obtener las palabras clave:', e)
        return None

def guardar_informacion(nombre_producto, calificaciones, palabras_clave):
    try:
        with open('compras.txt', 'a') as archivo:
            archivo.write(f'Nombre del producto: {nombre_producto}\n')
            archivo.write('Calificaciones: ')
            for calificacion in calificaciones:
                archivo.write(f'{calificacion.text} ')
            archivo.write('\nPalabras clave:\n')
            for palabra in palabras_clave:
                archivo.write(f'{palabra}\n')
            archivo.write('\n')
        print("Información guardada correctamente en 'compras.txt'")
    except Exception as e:
        print("Error al guardar la información:", e)

url = pyperclip.paste()
print("URL copiada del portapapeles:", url)

while True:
    if pyperclip.paste() != url:
        url = pyperclip.paste()
        nombre_producto = input('Ingrese el nombre del producto: ')
        calificaciones = obtener_calificaciones(url)
        if calificaciones:
            palabras_clave = obtener_palabras_clave(url)
            guardar_informacion(nombre_producto, calificaciones, palabras_clave)
        else:
            print("No se pudieron obtener las calificaciones.")
