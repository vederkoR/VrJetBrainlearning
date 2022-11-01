from hstest.stage_test import *
from hstest.test_case import TestCase

CheckResult.correct = lambda: CheckResult(True, '')
CheckResult.wrong = lambda feedback: CheckResult(False, feedback)

MIN_DATA_STR_LEN = 100
INSTRUCTION = 'Print a random string containing 0 or 1'


class GenRandTest(StageTest):
    def generate(self) -> List[TestCase]:
        return [TestCase(stdin=["1010101101010",
                                "1010100111001010010101001010100001010001",
                                '0',
                                '1',
                                '0',
                                '1',
                                '0',
                                '0',
                                '0',
                                '0',
                                '1',
                                '0',
                                '0',
                                '1',
                                '0',
                                '1',
                                '0',
                                '1',
                                '1',
                                '0',
                                '1',
                                '0',
                                '0',
                                '0',
                                '1',
                                '0',
                                '0',
                                '1',
                                '0',
                                '0',
                                '0',
                                '1',
                                '0',
                                '1',
                                '0',
                                '1',
                                '1',
                                '1',
                                '0',
                                '1',
                                '0',
                                '0',
                                '0',
                                '1',
                                '0',
                                '1',
                                '0',
                                '1',
                                '0',
                                '0',
                                '1',
                                '0',
                                '1',
                                '0',
                                '0',
                                '1',
                                '01'],
                         attach=100),
                TestCase(stdin=["1010101101010_some_wrong_symbols",
                                "1010100111001010010101001010100001010001_some_more_wrong_symbols",
                                '0',
                                '1',
                                '0',
                                '1',
                                '0',
                                '0',
                                '0',
                                '0',
                                '1',
                                '0',
                                '0',
                                '1',
                                '0',
                                '1',
                                '0',
                                '1',
                                '1',
                                '0',
                                '1',
                                '0',
                                '0',
                                '0',
                                '1',
                                '0',
                                '0',
                                '1',
                                '0',
                                '0',
                                '0',
                                '1',
                                '0',
                                '1',
                                '0',
                                '1',
                                '1',
                                '1',
                                '0',
                                '1',
                                '0',
                                '0',
                                '0',
                                '1',
                                '0',
                                '1',
                                '0',
                                '1',
                                '0',
                                '0',
                                '1',
                                '0',
                                '1',
                                '0',
                                '0',
                                '1',
                                '01'
                                ],
                         attach=100)
                ]

    def check(self, output: str, attach) -> CheckResult:
        strings = [s for s in output.split('\n') if s != '']
        if not strings:
            return CheckResult.wrong("The output seems to be empty.")

        instructions = strings[0]
        data_string = strings[-1]


        if INSTRUCTION.lower() not in instructions.lower():
            return CheckResult.wrong('Please give instructions to user in the form "{}"'.format(INSTRUCTION))
        if len(data_string) < MIN_DATA_STR_LEN:
            return CheckResult.wrong('Data string is too short, it should have length >={}'.format(MIN_DATA_STR_LEN))
        if len(data_string) != attach:
            return CheckResult.wrong("The string \"{}\" of your output is supposed to contain the final data string. \n"
                                     "However, it contains wrong number of symbols".format(data_string))
        if len(data_string) < 100:
            return CheckResult.wrong('Length of your output is too short.')
        if [s for s in data_string if s not in "10"]:
            return CheckResult.wrong("Wrong symbols are found in the final data string.")

        return CheckResult.correct()


if __name__ == '__main__':
    GenRandTest('predictor.predictor').run_tests()
