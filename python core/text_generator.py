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
    while True:
        key_name = input()
        if key_name == "exit":
            break
        print("Head:", key_name)
        try:
            for key, value in dict_words[key_name].items():
                print(f"Tail: {key} Count: {value}")
        except KeyError:
            print("Key Error. The requested word is not in the model. Please input another word.")




        # try:
        #     print(f"Head: {bigrm[int(token_num)][0]}    Tail: {bigrm[int(token_num)][1]}")
        # except TypeError:
        #     print("Type Error. Please input an integer.")
        # except IndexError:
        #     print("Index Error. Please input an integer that is in the range of the corpus.")
        # except ValueError:
        #     print("Value Error. Please input an integer from 0 to corpus size")
