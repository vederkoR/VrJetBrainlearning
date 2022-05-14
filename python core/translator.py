import sys

import requests

from bs4 import BeautifulSoup


class Translator:
    """This class represents a translator which is able to translate to 13 most popular languages \
     with multiple examples"""

    lang_pool = {"0": "All", "1": "Arabic", "2": "German", "3": "English", "4": "Spanish", "5": "French", "6": "Hebrew",
                 "7": "Japanese", "8": "Dutch", "9": "Polish", "10": "Portuguese", "11": "Romanian",
                 "12": "Russian", "13": "Turkish"}
    url_base = 'https://context.reverso.net/translation/'
    headers = {'User-Agent': 'Mozilla/5.0'}

    def __init__(self, in_from=None, in_to=None, arg_word=None):
        self.url = None
        self.index_to = None
        self.index_from = None
        self.to_translate = None
        self.translation_pair = None
        self.string_to_save = ''
        self.in_from = in_from
        self.in_to = in_to
        self.arg_word = arg_word

    def run(self):
        if self.in_from is None:
            print('Hello, welcome to the translator. Translator supports:')
            for k, v in Translator.lang_pool.items():
                print(f"{k}. {v}")
            self.params_set()
        else:
            self.index_from = str(list(Translator.lang_pool.values()).index(self.in_from.capitalize()))
            self.index_to = str(list(Translator.lang_pool.values()).index(self.in_to.capitalize()))
            self.to_translate = self.arg_word
        if self.index_to == "0":
            self.case_zero_action()
        else:
            self.case_not_zero_action()
        path = self.to_translate + ".txt"
        with open(path, mode='w') as file:
            file.write(self.string_to_save)

    def params_set(self):
        print("Type the number of your language:")
        self.index_from = input()
        print("Type the number of a language you want to translate to or '0' to translate to all languages:")
        self.index_to = input()
        print('Type the word you want to translate:')
        self.to_translate = input()

    @staticmethod
    def connection(url_inner, headers_inner):
        r = requests.get(url_inner, headers=headers_inner)
        while str(r.status_code) != "200":
            r = requests.get(url_inner, headers=headers_inner)
        soup = BeautifulSoup(r.content, "html.parser")
        return soup

    @staticmethod
    def lang_title_printer(lang_to):
        return f"{lang_to} Translations:"

    @staticmethod
    def example_title_printer(lang_to):
        return f"{lang_to} Examples:"

    def print_s(self, *args):
        for arg in args:
            self.string_to_save += arg
        self.string_to_save += '\n'
        print(*args)

    def case_zero_action(self):
        for lang in Translator.lang_pool.values():
            if lang == Translator.lang_pool[self.index_from]:
                continue
            if lang == "All":
                continue
            soup = self.soup_set(lang)
            if lang != "Arabic":
                self.print_s()
            self.print_s(Translator.lang_title_printer(lang))
            self.print_s(soup.find_all("span", class_="display-term")[0].text.strip())
            self.print_s()
            self.print_s(Translator.example_title_printer(lang))
            self.print_s(soup.find_all('div', class_="example")[0].text.strip().replace("\n\n\n\n\r\n          ", "\n")
                         .replace("\n\n\n\n\n", "\n"))
            self.print_s()

    def case_not_zero_action(self):
        soup = self.soup_set(Translator.lang_pool[self.index_to])
        self.print_s()
        self.print_s(Translator.lang_title_printer(Translator.lang_pool[self.index_to]))

        words = soup.find_all("span", class_="display-term")
        for word in words:
            self.print_s(word.text.strip())
        self.print_s()

        self.print_s(Translator.example_title_printer(Translator.lang_pool[self.index_to]))
        all_examples = soup.find_all('div', class_="example")
        flag = False
        for example in all_examples:
            if flag:
                self.print_s()
            self.print_s(example.text.strip().replace("\n\n\n\n\r\n          ", "\n").replace("\n\n\n\n\n", "\n"))
            flag = True

    def soup_set(self, lang_to):
        self.translation_pair = \
            f'{Translator.lang_pool[self.index_from].lower()}-{lang_to.lower()}'
        self.url = Translator.url_base + self.translation_pair + '/' + self.to_translate
        return Translator.connection(self.url, Translator.headers)


arguments = sys.argv
if len(arguments) > 1:
    translator = Translator(arguments[1], arguments[2], arguments[3])
else:
    translator = Translator()
translator.run()

