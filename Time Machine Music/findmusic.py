import requests
from bs4 import BeautifulSoup


def find_music(time):
    url = "https://www.billboard.com/charts/hot-100/" + time
    response = requests.get(url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, "html.parser")
    song_names_spans = soup.find_all("span", class_="chart-element__information__song")
    song_names = [song.getText() for song in song_names_spans]
    return song_names


