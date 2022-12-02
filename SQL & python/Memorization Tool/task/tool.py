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
    box_number = Column(Integer, default=1)


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


def practice_flashcards(session):
    global flashcards
    if not flashcards:
        print(sp.NO_FLASHCARDS)
    else:
        for flashcard in flashcards:
            print()
            print(sp.QUESTION, flashcard.question)
            while True:
                print(sp.REQUEST_READ_OR_MODIFY)
                y_n_u_selected = input()
                match y_n_u_selected:
                    case "n":
                        print("")
                        break
                    case "y":
                        print(sp.ANSWER, flashcard.answer)
                        box_placement(flashcard.flashcard_id, session)
                        break
                    case "u":
                        update_flashcard(flashcard.flashcard_id, session)
                        break
                    case _:
                        print(y_n_u_selected, sp.ERROR_REQUEST)


def ident_cur_card(f_id, session):
    query = session.query(Flashcard)
    current_fc_query = query.filter(Flashcard.flashcard_id == f_id)
    current_fc = current_fc_query.first()
    return current_fc_query, current_fc


def box_placement(f_id, session):
    current_fc_query, current_fc = ident_cur_card(f_id, session)
    while True:
        print(sp.LEARNING_MENU)
        is_correct = input()
        match is_correct:
            case 'y':
                print(current_fc.box_number)
                if current_fc.box_number == 3:
                    flashcards.remove(current_fc)
                    current_fc_query.delete()
                else:
                    current_fc_query.update({"box_number": current_fc.box_number + 1})
                session.commit()
                break
            case 'n':
                current_fc_query.update({"box_number": 1})
                session.commit()
                break
            case _:
                print(is_correct, sp.ERROR_REQUEST)


def update_flashcard(f_id, session):
    current_fc_query, current_fc = ident_cur_card(f_id, session)
    while True:
        print(sp.UPDATE_MENU)
        option_selected = input()
        match option_selected:
            case 'd':
                current_fc_query.delete()
                session.commit()
                break
            case 'e':
                print("current question:", current_fc.question)
                print("please write a new question:")
                new_question = input()
                print()

                print("current answer:", current_fc.answer)
                print("please write a new answer:")
                new_answer = input()
                print()

                if not new_question.strip():
                    new_question = current_fc.question

                if not new_answer.strip():
                    new_answer = current_fc.answer

                current_fc_query.update({"question": new_question, "answer": new_answer})
                session.commit()
                break
            case _:
                print(option_selected, sp.ERROR_REQUEST)


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
                practice_flashcards(session)

            case "3":
                print(sp.FAREWELL_WORDS)
                break
            case _:
                print(selected_main, sp.ERROR_REQUEST)


if __name__ == '__main__':
    main()
