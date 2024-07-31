import requests
from bs4 import BeautifulSoup
# from urllib.parse import urljoin

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

# Send a GET request to the URL
response = requests.get(URL)
website_html = response.text

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(website_html, 'html.parser')

# print(soup.prettify())
all_movies = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")
# print(all_movies)

movie_titles = [movie.getText() for movie in all_movies]
# print(movie_titles[::-1])
movies = movie_titles[::-1]

# for n in range(len(movie_titles)-1, 0, -1):
#     print(movie_titles[n])

with open("Python DAY/Codes/Day45/100 Movies that you must watch/movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")