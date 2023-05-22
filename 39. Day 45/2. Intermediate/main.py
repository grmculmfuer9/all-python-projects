from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(markup=yc_web_page, parser="html.parser", features="lxml")
span_anchor_tags = soup.find_all(name="span", class_="titleline")
article_texts = []
article_links = []
for article_tag in span_anchor_tags:
    article_text = article_tag.a.text
    article_link = article_tag.a.get("href")

    article_texts.append(article_text)
    article_links.append(article_link)

article_upvotes = [int(x.text.split()[0]) for x in soup.find_all(name="span", class_="score")]

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)
print(article_texts[largest_index])
print(article_links[largest_index])
