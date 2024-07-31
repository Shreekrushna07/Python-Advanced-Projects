
import requests

response = requests.get("https://news.ycombinator.com/news")
# response = requests.get("https://golden-days-universal-school.onrender.com")
# response = requests.get("https://hotelhindkesari.com/")
# print(response.text)

yc_web_page = response.text
soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.prettify())
print(soup.title)