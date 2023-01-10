from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.find_all(name="span", class_="titleline")
article_texts = []
articles_links = []
articles_upvotes = []

for article_tag in articles:
    text = article_tag.select_one("a").text
    article_texts.append(text)
    link = article_tag.select_one("a").get("href")
    articles_links.append(link)


for txt in soup.find_all(name="td", class_="subtext"):
    if txt.find(name="span", class_="subline") is None:
        upvote = 0
    else:
        upvote = int(txt.find(name="span", class_="subline").getText().split()[0])

    articles_upvotes.append(upvote)


print(article_texts)
print(articles_links)
print(articles_upvotes)

# Largest upvotes
largest_index = articles_upvotes.index(max(articles_upvotes))

print(article_texts[largest_index])
print(articles_links[largest_index])
print(articles_upvotes[largest_index])


