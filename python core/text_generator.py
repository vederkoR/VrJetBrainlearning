import nltk
from nltk.tokenize import WhitespaceTokenizer

# Write your code here
filename = input()
with open(filename, "r", encoding="utf-8") as file:
    text = file.read()
    tokens = WhitespaceTokenizer().tokenize(text)
    bigrm = list(nltk.bigrams(tokens))
    print("Number of bigrams:", len(bigrm))
    print()
    while True:
        token_num = input()
        if token_num == "exit":
            break
        try:
            print(f"Head: {bigrm[int(token_num)][0]}    Tail: {bigrm[int(token_num)][1]}")
        except TypeError:
            print("Type Error. Please input an integer.")
        except IndexError:
            print("Index Error. Please input an integer that is in the range of the corpus.")
        except ValueError:
            print("Value Error. Please input an integer from 0 to corpus size")
