import requests
import pyperclip
def save_html(html, numdownloads):
    name = f"web_page_{numdownloads}.txt"
    with open(name, "w") as file:
        file.write(html)
    print(f"Saved HTML to {name}")
numdownloads= 0
while True:
    try:
        url = pyperclip.paste()
        response = requests.get(url)
        response.raise_for_status()
        html = response.text
        save_html(html, numdownloads)
        numdownloads += 1
        break
    except requests.exceptions.RequestException as e:
        print('An error occurred while trying to fetch the webpage:', e)