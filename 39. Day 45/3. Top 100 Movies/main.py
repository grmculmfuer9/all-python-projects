import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(url=URL)
movies_web_page = response.text

soup = BeautifulSoup(markup=movies_web_page, parser="html.parser", features="lxml")

movies = soup.find_all(name="h3", class_="title")
movies_lst = [x.getText() for x in movies][::-1]

with open(file="movies.txt", mode="w", encoding="utf-8") as file:
    for x in movies_lst:
        file.write(f"{x}\n")
