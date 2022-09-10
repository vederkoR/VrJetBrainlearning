import os
import re
import requests
from bs4 import BeautifulSoup

pages = input()
type_ = input()
for p in range(1, int(pages)+1):
    page = str(p)
    folder = "Page_" + page
    os.mkdir(folder)

    url = "https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=" + page
    r = requests.get(url)

    soup = BeautifulSoup(r.text, 'lxml')
    round_1 = soup.find_all("article", class_="u-full-height c-card c-card--flush")
    list_news = [article for article in round_1 if type_ == article.find(class_="c-meta__type").text]
    if not list_news:
        continue
    for article in list_news:
        a_type = article.find("a")
        name = a_type.text
        link = a_type.get("href")
        full_link = "https://www.nature.com" + link
        correct_name = re.sub('[?!, ]', '_', name).strip("_") + '.txt'
        r = requests.get(full_link)
        soup = BeautifulSoup(r.text, 'lxml')
        round_2 = soup.find(class_='c-article-body u-clearfix').text.encode(encoding='utf-8')
        with open(folder + '\\' + correct_name, 'bw') as txt_file:
            txt_file.write(round_2)
print("Saved all articles.")