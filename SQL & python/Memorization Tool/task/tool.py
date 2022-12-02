from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, create_engine

import standard_phrases as sp

Base = declarative_base()
flashcards = []


class Flashcard(Base):
    __tablename__ = 'flashcard'

    flashcard_id = Column(Integer, primary_key=True)
    question = Column(String(100))
    answer = Column(String(100))


def add_manu(selected, session):
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
            new_flashcard = Flashcard(question=question, answer=answer)
            flashcards.append(new_flashcard)
            session.add(new_flashcard)
            session.commit()
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


def set_database():
    engine = create_engine("sqlite:///flashcard.db?check_same_thread=False")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()


def load_flashcard_list(session):
    global flashcards
    db_flashcards_list = session.query(Flashcard).all()
    if db_flashcards_list:
        flashcards.extend(session.query(Flashcard).all())


def main():
    session = set_database()
    load_flashcard_list(session)

    while True:
        print(sp.MAIN_MENU)
        selected_main = input()
        match selected_main:
            case "1":
                while True:
                    print(sp.ADD_MENY)
                    selected_add = input()
                    again = add_manu(selected_add, session)
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
