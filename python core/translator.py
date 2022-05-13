import requests

from bs4 import BeautifulSoup

print('Hello, welcome to the translator. Translator supports:')
lang_pool = {"1": "Arabic", "2": "German", "3": "English", "4": "Spanish", "5": "French", "6": "Hebrew",
             "7": "Japanese", "8": "Dutch", "9": "Polish", "10": "Portuguese", "11": "Romanian",
             "12": "Russian", "13": "Turkish"}
for k, v in lang_pool.items():
    print(f"{k}. {v}")
print("Type the number of your language:")
language_from_choice = input()
print("Type the number of language you want to translate to:")
language_to_choice = input()
print('Type the word you want to translate:')
word = input()
translation_pair = f'{lang_pool[language_from_choice].lower()}-{lang_pool[language_to_choice].lower()}'

url = 'https://context.reverso.net/translation/' + translation_pair + '/' + word
headers = {'User-Agent': 'Mozilla/5.0'}
r = requests.get(url, headers=headers)
while str(r.status_code) != "200":
    r = requests.get(url, headers=headers)
soup = BeautifulSoup(r.content, "html.parser")
print()
print(lang_pool[language_to_choice], "Translations:")
examples = []
all_ = soup.find_all('div', class_="example")
for one in all_:
    examples.append(one.text.strip().replace("\n\n\n\n\r\n          ", "\n"))

words = []

tr_words = soup.find_all("span", class_="display-term")
for tr_word in tr_words:
    words.append(tr_word.text.strip())

for single_word in words:
    print(single_word)

print()
print(lang_pool[language_to_choice], "Examples:")
j = 0
for example in examples:
    if j > 0:
        print()
    print(example)
    j += 1
