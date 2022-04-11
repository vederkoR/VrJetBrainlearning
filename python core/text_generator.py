import random
import re
import nltk
from nltk.tokenize import WhitespaceTokenizer

# Write your code here
filename = input()
with open(filename, "r", encoding="utf-8") as file:
    text = file.read()
    tokens = WhitespaceTokenizer().tokenize(text)
    bigrm = list(nltk.bigrams(tokens))
    dict_words = {}
    for pair in bigrm:
        dict_words.setdefault(pair[0], {})
        dict_words[pair[0]].setdefault(pair[1], 0)
        dict_words[pair[0]][pair[1]] += 1
    tokens_cap = [x for x in tokens if (x[0].isupper() and bool(re.fullmatch("[A-z'-]+", x)))]
    for _ in range(0, 10):
        word = random.choice(tokens_cap)
        phrase = ""
        phrase += word
        word_next = word
        for i in range(0, 4):
            word_next = \
                random.choices(list(dict_words[word_next].keys()), weights=list(dict_words[word_next].values()), k=1)[0]
            phrase += " " + word_next
        while ('.' not in word_next) and ('!' not in word_next) and ('?' not in word_next):
            word_next = \
                random.choices(list(dict_words[word_next].keys()), weights=list(dict_words[word_next].values()), k=1)[0]
            phrase += " " + word_next
        print(phrase)
