import requests

from bs4 import BeautifulSoup

print('Type "en" if you want to translate from French into English, or "fr" if you want to /'
      'translate from English into French:')
language_choice = input()
print('Type the word you want to translate:')
word = input()
print(f'You chose "{language_choice}" as the language to translate "{word}".')
translation_pair = ''

if language_choice == "fr":
    translation_pair = 'english-french'
else:
    translation_pair = 'french-english'
url = 'https://context.reverso.net/translation/' + translation_pair + '/' + word
headers = {'User-Agent': 'Mozilla/5.0'}
r = requests.get(url, headers=headers)
while str(r.status_code) != "200":
    r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, "html.parser")
print("200 OK")
print("Translations")
examples = []
all_ = soup.find_all('div', class_="ltr")
for one in all_:
    examples.append(one.text.strip())

words = []

tr_words = soup.find_all("span", class_="display-term")
for tr_word in tr_words:
    words.append(tr_word.text.strip())

print(words)
print(examples)
