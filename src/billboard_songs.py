import requests
import csv
from bs4 import BeautifulSoup


def get_top_100_songs():
    url = "https://www.billboard.com/charts/year-end/hot-100-songs"
    html_content = requests.get(url).text

    soup = BeautifulSoup(html_content, "lxml")

    titles = [title.text.replace('\n','') for title in soup.findAll("div", attrs={"class": "ye-chart-item__title"})]
    artists = [artist.text.replace('\n','') for artist in soup.findAll("div", attrs={"class": "ye-chart-item__artist"})]
    
    return dict(zip(titles, artists))


def get_non_hits():
    non_hits = {}

    with open('non_hits.csv', 'r') as csv_file:
        for line in csv_file.readlines():
            col = line[0].split()
            title = col[0].replace('\n','')
            artist = col[1].replace('\n','')
            non_hits[title] = artist
        return non_hits
    
    # File did not open, return empty
    return {}

# Title:
# <div class="ye-chart-item__title"> {Title}

# Artist
# <div class="ye-chart-item__artist">
# <a href="/music/the-weeknd"> {Artist} </a>