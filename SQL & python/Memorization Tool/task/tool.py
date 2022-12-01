# write your code here
import standard_phrases as sp

flashcards = []


class Flashcard:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


def add_manu(selected):
    global flashcards
    print()
    match selected:
        case "1":
            while True:
                print(sp.QUESTION)
                question = input()
                if question.strip() != '':
                    break
            while True:
                print(sp.ANSWER)
                answer = input()
                if answer.strip() != '':
                    break
            flashcards.append(Flashcard(question=question, answer=answer))
        case "2":
            return False
        case _:
            print(selected, sp.ERROR_REQUEST)
    return True


def practice_flashcards():
    global flashcards
    if not flashcards:
        print(sp.NO_FLASHCARDS)
    else:
        for flashcard in flashcards:
            print()
            print(sp.QUESTION, flashcard.question)
            print(sp.REQUEST_TO_SHOW_ANSWER)
            y_n_selected = input()
            match y_n_selected:
                case "n":
                    print("")
                case "y":
                    print(sp.ANSWER, flashcard.answer)
                case _:
                    print(y_n_selected, sp.ERROR_REQUEST)


def main():
    while True:
        print(sp.MAIN_MENU)
        selected_main = input()
        match selected_main:
            case "1":
                while True:
                    print(sp.ADD_MENY)
                    selected_add = input()
                    again = add_manu(selected_add)
                    if not again:
                        break
            case "2":
                practice_flashcards()

            case "3":
                print(sp.FAREWELL_WORDS)
                break
            case _:
                print(selected_main, sp.ERROR_REQUEST)


if __name__ == '__main__':
    main()
