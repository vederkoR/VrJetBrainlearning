import re

variables = dict()
if __name__ == "__main__":
    while True:
        user_input = input().strip()
        if user_input == '':
            continue
        elif user_input == '/exit':
            break
        elif user_input == '/help':
            print("The program calculates the sum of numbers")
            continue
        elif user_input.startswith("/"):
            print("Unknown command")
            continue
        flag = False
        for k, v in variables.items():
            if flag:
                break
            if "=" not in user_input:
                user_input = user_input.replace(k, v)
            else:
                temp = user_input.split("=", 1)
                user_input = "=".join([temp[0], temp[1].replace(k, v)])
        if "//" in user_input:
            print("Invalid expression")
        if "=" in user_input:
            temp = user_input.split("=", 1)
            try:
                user_input = "=".join([temp[0], str(eval(temp[1]))])
            except NameError:
                print("Unknown variable")
                continue
            except SyntaxError:
                print("Invalid assignment")
                continue
        match = re.fullmatch(r'(\w+)\s*=\s*(-?\d+)', user_input, flags=re.ASCII)
        if match:
            if match.group(1).isalpha():
                variables[match.group(1)] = match.group(2)
                continue
            else:
                print("Invalid identifier")
                continue
        if "=" in user_input:
            print("Invalid identifier")
            continue
        try:
            temp = eval(user_input)
            if isinstance(temp, float) and temp.is_integer():
                print(int(temp))
            else:
                print(temp)
        except ValueError:
            print("Invalid expression")
        except NameError:
            print("Unknown variable")
        except SyntaxError:
            print("Invalid expression")

print("Bye!")
