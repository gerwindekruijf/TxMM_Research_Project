import requests
import csv
from bs4 import BeautifulSoup
from pathlib import Path


def get_top_100_songs():
    url = "https://www.billboard.com/charts/year-end/2020/hot-100-songs"
    # https://www.billboard.com/charts/year-end/2019/hot-100-songs
    html_content = requests.get(url).text

    soup = BeautifulSoup(html_content, "lxml")

    titles = [title.text.replace('\n','') for title in soup.findAll("div", attrs={"class": "ye-chart-item__title"})]
    artists = [artist.text.replace('\n','') for artist in soup.findAll("div", attrs={"class": "ye-chart-item__artist"})]

    if len(titles) != 100 or len(artists) != 100:
        print("Couldn't load all the data from billboard")
    
    return list(zip(titles, artists))


def get_non_hits():
    non_hits = []
    path = str(Path().resolve().parent)
    
    with open(f'{path}/data/non_hits.csv', 'r') as csv_file:
        for line in csv_file.readlines()[1:]:
            cols = line.rstrip().split(',')
            title = cols[0]
            artist = cols[1]
            non_hits.append((title, artist))
    
    return non_hits

get_top_100_songs()
# Title:
# <div class="ye-chart-item__title"> {Title}

# Artist
# <div class="ye-chart-item__artist">
# <a href="/music/the-weeknd"> {Artist} </a>