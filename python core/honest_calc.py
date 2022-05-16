class RudeCommenter:
    msg_0 = "Enter an equation"
    msg_1 = "Do you even know what numbers are? Stay focused!"
    msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
    msg_3 = "Yeah... division by zero. Smart move..."
    msg_4 = "Do you want to store the result? (y / n):"
    msg_5 = "Do you want to continue calculations? (y / n):"

    def __init__(self):
        self.equation = None
        self.first_var = None
        self.second_var = None
        self.sign = None
        self.memory = 0.0
        self.on = True
        self.result = None

    def run(self):
        while self.on:
            self.process()

    def process(self):
        while True:
            self.set_equation()
            if not (self.first_var.replace(".", "", 1).replace("-", "", 1).isnumeric()
                    and self.second_var.replace(".", "", 1).replace("-", "", 1).isnumeric()):
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
            self.memory = self.result

    def cont_calc(self):
        print(RudeCommenter.msg_5)
        inner_choice = input()
        if inner_choice != "y":
            self.on = False


def main():
    rude_commenter = RudeCommenter()
    rude_commenter.run()


if __name__ == '__main__':
    main()
