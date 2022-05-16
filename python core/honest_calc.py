class RudeCommenter:
    msg_0 = "Enter an equation"
    msg_1 = "Do you even know what numbers are? Stay focused!"
    msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"

    def __init__(self):
        self.equation = None
        self.first_var = None
        self.second_var = None
        self.sign = None

    def run(self):
        while True:
            self.set_equation()
            if not (self.first_var.replace(".", "", 1).isnumeric() and self.second_var.replace(".", "", 1)
                    .isnumeric()):
                print(RudeCommenter.msg_1)
                continue
            if self.sign not in r"+-*/":
                print(RudeCommenter.msg_2)
                continue
            break

    def set_equation(self):
        print(RudeCommenter.msg_0)
        self.equation = input()
        self.first_var, self.sign, self.second_var = self.equation.split()


def main():
    rude_commenter = RudeCommenter()
    rude_commenter.run()


if __name__ == '__main__':
    main()
