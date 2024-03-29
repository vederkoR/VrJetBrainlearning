from typing import List

from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult

RIGHT_OUTPUT = """
Today:
1) Do yoga
2) Make a breakfast
3) Learn the basics of SQL
4) Learn about ORM
"""


class ToDoList(StageTest):
    def generate(self) -> List[TestCase]:
        return [
            TestCase()
        ]

    def check(self, reply, attach):
        if reply.strip() == RIGHT_OUTPUT.strip():
            return CheckResult.correct()
        else:
            return CheckResult.wrong('Your output should be like in example!\n'
                                     ' Make sure you didn\'t print any extra spaces')


if __name__ == '__main__':
    ToDoList('todolist.todolist').run_tests()
