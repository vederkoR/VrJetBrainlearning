from hstest.stage_test import StageTest
from hstest.test_case import TestCase
from hstest.check_result import CheckResult
import re


class CCATest(StageTest):

    def generate(self):
        return [TestCase(time_limit=60000)]

    def check(self, reply, attach):
        lines = reply.split('\n')
        if "" in lines:
            lines = list(filter(lambda a: a != "", lines))

        # general
        if len(lines) < 4:
            return CheckResult.wrong(
                feedback="There is not enough lines in the answer, check the example output at the stage 1")
        if 'class' not in lines[0].lower() \
            or 'feature' not in lines[1].lower() \
            or 'target' not in lines[2].lower() \
            or not all(key_word in lines[3].lower() for key_word in ['min', 'max']):
            return CheckResult.wrong(
                feedback="Something is wrong with the order of answers, check the example output at the stage 1")

        # 1st question
        classes_reply = list(map(float, re.findall(r'\d*\.\d+|\d+', lines[0])))
        if set(classes_reply) != set([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
            return CheckResult.wrong(feedback="Wrong set of target classes")
        if len(classes_reply) != len(set(classes_reply)):
            return CheckResult.wrong(feedback="There are some duplicates in the list of classes")

        # 2nd question
        features_shape_reply = list(map(float, re.findall(r'\d*\.\d+|\d+', lines[1])))
        if len(features_shape_reply) != 2:
            return CheckResult.wrong(feedback="The shape of features should consist of 2 numbers")
        if features_shape_reply[0] != 60000:
            return CheckResult.wrong(feedback="Wrong number of rows in features' array")
        if features_shape_reply[1] != 784:
            return CheckResult.wrong(feedback="Wrong number of columns in features' array")

        # 3rd question
        target_shape_reply = list(map(float, re.findall(r'\d*\.\d+|\d+', lines[2])))
        if len(target_shape_reply) != 1:
            return CheckResult.wrong(feedback="The shape of the target variable should consist of 1 number")
        if target_shape_reply[0] != 60000:
            return CheckResult.wrong(feedback="Wrong number of rows in the target variable")

        # 4th question
        minmax_reply = list(map(float, re.findall(r'\d*\.\d+|\d+', lines[3])))
        if len(minmax_reply) != 2:
            return CheckResult.wrong(feedback="It should be 2 numbers in the last line of answer")
        if min(minmax_reply) != 0:
            return CheckResult.wrong(feedback="The minimum number is wrong")
        if max(minmax_reply) != 255:
            return CheckResult.wrong(feedback="The maximum number is wrong")

        return CheckResult.correct()


if __name__ == '__main__':
    CCATest().run_tests()
