import requests
from bs4 import BeautifulSoup

url = input('Input the URL:')
r = requests.get(url)

if r:
    content = r.content
    with open('source.html', 'wb') as file:
        file.write(content)
        print("Content saved.")

else:
    print(f'The URL returned {r.status_code}')
