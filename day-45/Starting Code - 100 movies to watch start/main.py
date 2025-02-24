import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
movies_html = response.text

soup = BeautifulSoup(movies_html, "html.parser")
movies = soup.find_all(name="h3", class_="title")
movies_titles = [movie.getText().replace(")", ".") for movie in movies]

with open("movies.txt", mode="w") as file:
    for movie in movies_titles[::-1]:
        file.write(f"{movie}\n")
