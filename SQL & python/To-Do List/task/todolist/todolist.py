from datetime import datetime
from sqlalchemy import create_engine, Column, String, Integer, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Query

Base = declarative_base()
today_tasks = []
MAIN_MENU = """1) Today's tasks
2) Add a task
0) Exit"""


class Task(Base):
    __tablename__ = 'task'

    id = Column(Integer, primary_key=True)
    task = Column(String)
    deadline = Column(Date, default=datetime.today())


def connect_sql_alchemy():
    engine = create_engine('sqlite:///todo.db?check_same_thread=False')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()


def load_tasks(session):
    query = Query(Task, session)
    all_rows = query.all()

    for row in all_rows:
        today_tasks.append(Task(id=row.id, task=row.task, deadline=row.deadline))


def add_task(session):
    print("Enter a task")
    task_to_add_text = input()
    task_to_add = Task(task=task_to_add_text)
    today_tasks.append(task_to_add)
    session.add(task_to_add)
    session.commit()


def display_tasks():
    print("Today:")
    if not today_tasks:
        print('Nothing to do!')
        print()
        return
    for inx, item in enumerate(today_tasks):
        print(f"{inx + 1}) {item.task}")
    print()


def main():
    session = connect_sql_alchemy()

    load_tasks(session)
    while True:
        print(MAIN_MENU)
        selected = input()
        print()
        match selected:
            case '1':
                display_tasks()
            case '2':
                add_task(session)
            case '0':
                print("\nBye!")
                break


if __name__ == '__main__':
    main()
    