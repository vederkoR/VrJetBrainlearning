from datetime import datetime, timedelta
from sqlalchemy import create_engine, Column, String, Integer, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Query

Base = declarative_base()
all_tasks = []
MAIN_MENU = """1) Today's tasks
2) Week's tasks
3) All tasks
4) Add a task
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
        all_tasks.append(Task(id=row.id, task=row.task, deadline=row.deadline))


def add_task(session):
    print("Enter a task")
    task_to_add_text = input()
    print("Enter a deadline")
    date_to_add_str = input()
    print()
    date_to_add_time = datetime.strptime(date_to_add_str, "%Y-%m-%d").date()
    task_to_add = Task(task=task_to_add_text, deadline=date_to_add_time)
    all_tasks.append(task_to_add)
    session.add(task_to_add)
    session.commit()


def display_tasks(lst):
    if not lst:
        print('Nothing to do!')
        print()
        return
    for inx, item in enumerate(lst):
        print(f"{inx + 1}. {item.task}")
    print()


def display_weekly_tasks():
    day = datetime.today().date()
    i = 0
    while i != 7:
        print(datetime.strftime(day, '%A %d %b:'))
        display_tasks([j for j in all_tasks if j.deadline == day])
        i += 1
        day += timedelta(days=1)


def display_all_tasks():
    if not all_tasks:
        print('Nothing to do!')
        print()
        return
    all_tasks.sort(key=lambda x: x.deadline)
    for inx, item in enumerate(all_tasks):
        print(f"{inx + 1}. {item.task}.", datetime.strftime(item.deadline, "%#d %b"))
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
                print(datetime.strftime(datetime.today().date(), "Today %#d %b"))
                display_tasks([j for j in all_tasks if j.deadline == datetime.today().date()])
            case '2':
                display_weekly_tasks()
            case '3':
                print("All tasks")
                display_all_tasks()
            case '4':
                add_task(session)
            case '0':
                print("\nBye!")
                break


if __name__ == '__main__':
    main()