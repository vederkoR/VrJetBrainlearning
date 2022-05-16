class RudeCommenter:
    msg_0 = "Enter an equation"
    msg_1 = "Do you even know what numbers are? Stay focused!"
    msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
    msg_3 = "Yeah... division by zero. Smart move..."
    msg_4 = "Do you want to store the result? (y / n):"
    msg_5 = "Do you want to continue calculations? (y / n):"
    msg_6 = " ... lazy"
    msg_7 = " ... very lazy"
    msg_8 = " ... very, very lazy"
    msg_9 = "You are"
    msg_10 = "Are you sure? It is only one digit! (y / n)"
    msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
    msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"

    def __init__(self):
        self.equation = None
        self.first_var = None
        self.second_var = None
        self.sign = None
        self.memory = 0.0
        self.on = True
        self.result = None
        self.msg = ''

    def run(self):
        while self.on:
            self.process()

    def process(self):
        while True:
            self.set_equation()
            self.msg = ''
            self.msg_adder()
            if self.msg != 0:
                print(self.msg)
            if not self.correctness_check():
                print(RudeCommenter.msg_1)
                continue
            if self.sign not in r"+-*/":
                print(RudeCommenter.msg_2)
                continue
            if self.sign == "/" and float(self.second_var) == 0:
                print(RudeCommenter.msg_3)
                continue
            self.operation()
            print(self.result)
            self.save()
            self.cont_calc()
            break

    def correctness_check(self):
        return (self.first_var.replace(".", "", 1).replace("-", "", 1).isnumeric() and
                self.second_var.replace(".", "", 1).replace("-", "", 1).isnumeric())

    def set_equation(self):
        print(RudeCommenter.msg_0)
        self.equation = input()
        self.first_var, self.sign, self.second_var = self.equation.split()
        if self.first_var == "M":
            self.first_var = str(self.memory)
        if self.second_var == "M":
            self.second_var = str(self.memory)

    def operation(self):
        if self.sign == "/":
            self.result = float(self.first_var) / float(self.second_var)
        elif self.sign == "*":
            self.result = float(self.first_var) * float(self.second_var)
        elif self.sign == "+":
            self.result = float(self.first_var) + float(self.second_var)
        else:
            self.result = float(self.first_var) - float(self.second_var)

    def save(self):
        print(RudeCommenter.msg_4)
        inner_choice = input()
        if inner_choice == "y":
            if self.one_digit_checker(self.result):
                print(RudeCommenter.msg_10)
                inner_choice = input()
                if inner_choice == "y":
                    print(RudeCommenter.msg_11)
                    inner_choice = input()
                    if inner_choice == "y":
                        print(RudeCommenter.msg_12)
                        inner_choice = input()
                        if inner_choice == "n":
                            return
                    else:
                        return
                else:
                    return
            self.memory = self.result

    def cont_calc(self):
        print(RudeCommenter.msg_5)
        inner_choice = input()
        if inner_choice != "y":
            self.on = False

    def msg_adder(self):
        if self.correctness_check():
            if RudeCommenter.one_digit_checker(float(self.first_var)) and \
                    RudeCommenter.one_digit_checker(float(self.second_var)):
                self.msg += RudeCommenter.msg_6
            if self.sign == '*' and (float(self.first_var) == 1 or float(self.second_var) == 1):
                self.msg += RudeCommenter.msg_7
            if (float(self.first_var) == 0 or float(self.second_var) == 0) and self.sign in r'*+-':
                self.msg += RudeCommenter.msg_8
        if self.msg != '':
            self.msg = RudeCommenter.msg_9 + self.msg

    @staticmethod
    def one_digit_checker(digit: float) -> bool:
        return bool(digit.is_integer() and digit in range(-9, 10))


def main():
    rude_commenter = RudeCommenter()
    rude_commenter.run()


if __name__ == '__main__':
    main()