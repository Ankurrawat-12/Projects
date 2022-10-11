from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text
soup = BeautifulSoup(yc_webpage, "html.parser")


articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

article_upvote = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]


i = article_upvote.index(max(article_upvote))
print(i)
print(article_texts)
print(article_links)
print(article_upvote)

# import lxml
# from bs4 import BeautifulSoup
# soup = BeautifulSoup(contents, "lxml")
#
#
# with open("website.html", encoding="utf-8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.string)
# print(soup.prettify())
# print(soup.p)
#
# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)
# for tag in all_anchor_tags:
#     print(tag.getText())
#     print(tag.get("href"))
#
# h1_heading = soup.find(name="h1", id="name")
#
# print(h1_heading)
#
# section_heading = soup.find(name="h3", class_="heading")
#
# print(section_heading.getText())
# print(section_heading.get("class"))
#
# print(soup.find_all(name="a"))
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# name = soup.select_one(selector="#name")
# print(name)
#
# heading = soup.select_one(selector=".heading")
# print(heading)
