import requests
from bs4 import BeautifulSoup
import csv



def get_html(url):
    r = requests.get(url)    # Получим метод Response
    return r.text   # Вернем данные объекта text


def csv_read(data):
    with open("song.csv", 'a') as file:
        writer = csv.writer(file)
        writer.writerow([data['original'],data['translate']])

def get_link(html):
    soup = BeautifulSoup(html, 'lxml')
    song = soup.find('div', id='click_area').find_all('div', class_="string_container")

    for i in song:
        original = i.find('div', class_='original').string + "  "
        translate = i.find('div', class_='translate').string

        data = {'original': original,
                 'translate': translate}
        csv_read(data)


data = get_link(get_html('https://www.amalgama-lab.com/songs/f/flo_rida/whistle.html'))
