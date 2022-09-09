import re
import requests
from bs4 import BeautifulSoup

url = "https://www.nature.com/nature/articles?sort=PubDate&year=2020&page=3"
r = requests.get(url)

soup = BeautifulSoup(r.text, 'lxml')
round_1 = soup.find_all("article", class_="u-full-height c-card c-card--flush")
list_news = [article for article in round_1 if "News" in article.text and not ("News Feature" in article.text)]
list_to_present = []
for article in list_news:
    a_type = article.find("a")
    name = a_type.text
    link = a_type.get("href")
    full_link = "https://www.nature.com" + link
    correct_name = re.sub('[?!, ]', '_', name).strip("_") + '.txt'
    list_to_present.append(correct_name)
    r = requests.get(full_link)
    soup = BeautifulSoup(r.text, 'lxml')
    round_2 = soup.find(class_='c-article-body u-clearfix').text.encode(encoding='utf-8')
    with open(correct_name, 'bw') as txt_file:
        txt_file.write(round_2)
print("Saved articles:")
print(list_to_present)