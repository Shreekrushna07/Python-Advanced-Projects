from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
# response = requests.get("https://golden-days-universal-school.onrender.com")
# response = requests.get("https://hotelhindkesari.com/")
# print(response.text)

yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")
print(soup.prettify())
# print(soup.title)

# article_tag = soup.find(name="a", class_="storyLink")
# article_tag = soup.find(name="a")
# print(article_tag)
# print(article_tag.getText())
# article_text = article_tag.getText() 
# article_link = article_tag.get("href")
# article_upvote = soup.find(name="span", class_="score").getText()