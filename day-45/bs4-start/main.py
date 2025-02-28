import requests
from bs4 import BeautifulSoup

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
article_texts = []
article_links = []

articles = soup.find_all(name="a", class_="storylink")

for article in articles:
    text = article.getText()
    link = article.get("href")
    article_texts.append(text)
    article_links.append(link)

article_upvotes = [
    int(score.getText().split()[0])
    for score in soup.find_all(name="span", class_="score")
]
most_voted_article_index = article_upvotes.index(max(article_upvotes))


print(article_texts[most_voted_article_index])
print(article_links[most_voted_article_index])
print(article_upvotes[most_voted_article_index])
