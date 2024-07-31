from bs4 import BeautifulSoup
import lxml

with open("Day45/bs4-start/website.html", encoding="utf-8") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

# print(soup)
# print(soup.title)
# print(soup.title.string)
# print(soup.title.name)  #name of tag
# print(soup)
# print(soup.prettify())
# print(soup.p)     

# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# all_anchor_tags = soup.find_all(name="a")
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))

# all_paragraph_tag = soup.find_all(name="p")
# print(all_paragraph_tag)


# heading = soup.find(name="h1", id="name")
# print(heading)

section_heading =soup.find(name="h3", class_="heading")
# print(section_heading.name)
# print(section_heading)
# print(section_heading.get("class"))


# company_url = soup.select_one(selector="p a")
# print(company_url)

# name = soup.select_one(selector="#name")
# print(name)

# headings = soup.select(".heading")
# print(headings)

class_is_heading = soup.find_all(class_ = "heading")
print(class_is_heading)