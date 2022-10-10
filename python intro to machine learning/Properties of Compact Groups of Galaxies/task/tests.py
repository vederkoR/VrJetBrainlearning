from hstest import *
from math import isclose
# import re


# def is_float(element):
#     if re.match(r'([+-]?(?:[0-9]*[.])?[0-9]+)', element) is None:
#         return False
#     else:
#         return True


def is_float(num: str):
    try:
        float(num)
        return True
    except ValueError:
        return False


class Stage1Test(PlottingTest):
    def check_outputs_number(self, values_number: int, user_output: str):
        outputs = user_output.split()

        if not all(is_float(output) for output in outputs):
            raise WrongAnswer(f"Answer '{user_output}' contains non-numeric values.")

        if len(outputs) != values_number:
            raise WrongAnswer(f"Answer contains {len(outputs)} values, but {values_number} values are expexted.")

    def check_num_values(self, values: list, user_values: list, message: str, rel_tol=1.0e-3):
        if not all(isclose(value, user_value, rel_tol=rel_tol) for value, user_value in zip(values, user_values)):
            raise WrongAnswer(message)

    @dynamic_test
    def test(self):
        pr = TestedProgram()
        user_output = pr.start().strip()

        if len(user_output.strip()) == 0:
            raise WrongAnswer("Seems like your program does not show any output.")

        # check output format
        self.check_outputs_number(2, user_output)

        # check values
        user_values = [float(value) for value in user_output.split()]

        first_value = [26.678053926691177]
        self.check_num_values(first_value, user_values[:1],
                              "The first submitted value (mean of mean surface brightness of the IGL for a groups with features) is wrong.\n"
                              "Make sure that you provide numbers in the correct order.",
                              rel_tol=1.0e-2)

        first_value = [27.038330296424938]
        self.check_num_values(first_value, user_values[1:2],
                              "The second submitted value (mean of mean surface brightness of the IGL for a groups without features) is wrong.\n"
                              "Make sure that you provide numbers in the correct order.",
                              rel_tol=1.0e-2)

        return CheckResult.correct()


if __name__ == '__main__':
    Stage1Test().run_tests()
