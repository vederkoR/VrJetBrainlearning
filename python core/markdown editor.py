commands = ["plain", "bold", "italic", "header", "link", "inline-code", "ordered-list",
            "unordered-list", "new-line"]


def list_commands():
    print("Available formatters:", *commands)
    print("Special commands: !help !done")


list_commands()


if __name__ == "__main__":
    while True:
        command = input("Choose a formatter: ")
        if command == "!done":
            break
        elif command == "!help":
            list_commands()
        elif command not in commands:
            print("Unknown formatting type or command")