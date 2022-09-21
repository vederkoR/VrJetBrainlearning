from hstest.stage_test import List
from hstest import StageTest, CheckResult, TestCase
import re

def get_number(string):
    return list(map(float, re.findall(r'-*\d*\.\d+|-*\d+', string)))


class LinearRegression(StageTest):

    def generate(self) -> List[TestCase]:
        return [
            TestCase(stdin="", attach=("", ""), time_limit=900000)
        ]

    def check(self, reply: str, attach):

        reply = reply.strip().split("\n")

        if len(reply) == 0:
            return CheckResult.wrong("No output was printed. Print output in the right format.")

        if len(reply) != 1:
            return CheckResult.wrong("Wrong output format. Check the Example section.")

        reply = reply[0]

        if 'array' not in reply:
            return CheckResult.wrong("Return coefficient(s) in numpy array")

        if reply.count(',') != 1 or reply.count(':') != 2 or reply.count('}') != reply.count('{'):
            return CheckResult.wrong('The dictionary output is not properly constructed.')

        output = reply.replace("{", "").replace("}", "").replace("'", '').lower().split(",")

        if len(output) != 2:
            return CheckResult.wrong(f"No of items in dictionary should be 2, {len(output)} present")

        output1, output2 = output
        name1, answer1 = output1.strip().split(':')
        name2, answer2 = output2.strip().split(':')
        answers = {name1.strip(): answer1.strip(), name2.strip(): answer2.strip()}
        intercept = answers.get('intercept', '0000000')
        coefficient = answers.get('coefficient', '0000000')
        coefficient = re.sub('array', '', coefficient)

        if intercept == '0000000' or coefficient == '0000000' or len(intercept) == 0 or len(coefficient) == 0:
            return CheckResult.wrong("Print values for both Intercept and Coefficient")

        intercept = get_number(intercept)
        if len(intercept) != 1:
            return CheckResult.wrong(f"Intercept should contain a single value, found {len(intercept)}")
        intercept = intercept[0]
        if not -2.8 < intercept < -2.6:
            return CheckResult.wrong("Wrong value for Intercept")

        coefficient = get_number(coefficient)
        if len(coefficient) != 1:
            return CheckResult.wrong(f"Coefficient should contain a single value, found {len(coefficient)}")
        if not 9.45 < coefficient[0] < 9.55:
            return CheckResult.wrong("Wrong value for beta1")

        return CheckResult.correct()


if __name__ == '__main__':
    LinearRegression().run_tests()
