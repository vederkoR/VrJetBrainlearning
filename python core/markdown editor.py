class MarkdownEditor:
    commands = ["plain", "bold", "italic", "header", "link", "inline-code", "new-line"]

    def __init__(self):
        self.full_text = ""

    def update(self, string):
        self.full_text += string

    @staticmethod
    def list_commands():
        print("Available formatters:", *MarkdownEditor.commands)
        print("Special commands: !help !done")

    @staticmethod
    def bold(string):
        return "".join(["**", string, "**"])

    @staticmethod
    def header_1(string: str, lvl: int):
        return "".join(["\n", lvl * "#", " ", string, "\n"])

    @staticmethod
    def header_2(string: str, lvl: int):
        return "".join([lvl * "#", " ", string, "\n"])

    @staticmethod
    def italic(string):
        return "".join(["*", string, "*"])

    @staticmethod
    def inline(string):
        return "".join(["`", string, "`"])

    @staticmethod
    def link(url_, string):
        return f"[{string}]({url_})"


if __name__ == "__main__":
    editor = MarkdownEditor()
    while True:
        flag = False
        command = input("Choose a formatter: ")
        if command == "!done":
            break
        elif command == "!help":
            MarkdownEditor.list_commands()
        elif command == "plain":
            text = input("Text:")
            editor.update(text)
        elif command == "bold":
            text = input("Text:")
            editor.update(MarkdownEditor.bold(text))
        elif command == "inline-code":
            text = input("Text:")
            editor.update(MarkdownEditor.inline(text))
        elif command == "italic":
            text = input("Text:")
            editor.update(MarkdownEditor.italic(text))
        elif command == "header":
            while True:
                level = int(input("Level:"))
                if level in range(1, 7):
                    break
                else:
                    print("The level should be within the range of 1 to 6")
            text = input("Text:")
            if editor.full_text == "":
                editor.update(MarkdownEditor.header_2(text, level))
            else:
                editor.update(MarkdownEditor.header_1(text, level))
        elif command == "link":
            label = input("Label:")
            url = input("URL:")
            editor.update(MarkdownEditor.link(url, label))
        elif command == "new-line":
            editor.update("\n")
        else:
            print("Unknown formatting type or command")
        print(editor.full_text)
