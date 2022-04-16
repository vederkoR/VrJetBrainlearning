import random
import re
import nltk
from nltk import ngrams
from nltk.tokenize import WhitespaceTokenizer

# Write your code here
filename = input()
with open(filename, "r", encoding="utf-8") as file:
    text = file.read()
    tokens = WhitespaceTokenizer().tokenize(text)
    bigrm = list(nltk.bigrams(tokens))
    trgrn = list(ngrams(tokens, 3))
    dict_words = {}
    for pair in trgrn:
        pair_1 = pair[0] + " " + pair[1]
        pair_2 = pair[2]
        dict_words.setdefault(pair_1, {})
        dict_words[pair_1].setdefault(pair_2, 0)
        dict_words[pair_1][pair_2] += 1
    tokens_cap = [x for x in trgrn if (x[0][0].isupper() and bool(re.fullmatch("[A-z'-]+", x[0])))]
    for _ in range(0, 10):
        words = random.choice(tokens_cap)
        phrase = " ".join(words)
        words_pair = words[1] + " " + words[2]
        for i in range(0, 2):
            word_next = \
                random.choices(list(dict_words[words_pair].keys()), weights=list(dict_words[words_pair].values()), k=1)[
                    0]
            phrase += " " + word_next
            words_pair = phrase.split()[-2] + " " + phrase.split()[-1]
        while ('.' != phrase[-1]) and ('!' != phrase[-1]) and ('?' != phrase[-1]):
            word_next = \
                random.choices(list(dict_words[words_pair].keys()), weights=list(dict_words[words_pair].values()),
                               k=1)[
                    0]
            phrase += " " + word_next
            words_pair = phrase.split()[-2] + " " + phrase.split()[-1]
        print(phrase)
