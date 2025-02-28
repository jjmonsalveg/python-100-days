from os import name

from bs4 import BeautifulSoup

with open("website.html", mode="r") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")

all_member_tags = soup.find_all(name="a")

for tag in all_member_tags:
    print(tag.getText())
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

h3_heading = soup.find(name="h3", class_="heading")
print(h3_heading.getText)

company_url = soup.select_one(selector="p a")
print(company_url)

name = soup.select_one(selector="#name")
print(name)

headings = soup.select_one(selector=".heading")
print(headings)
