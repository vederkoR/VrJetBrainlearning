class MenuDisplay:
    @staticmethod
    def display_main():
        print("MAIN MENU\n0 Exit\n1 CRUD operations\n2 Show top ten companies by criteria\n")

    @staticmethod
    def display_crud():
        print("CRUD MENU\n0 Back\n1 Create a company\n2 Read a company\n3 Update a company\n" +
              "4 Delete a company\n5 List all companies")

    @staticmethod
    def display_top_ten():
        print("TOP TEN MENU\n0 Back\n1 List by ND/EBITDA\n2 List by ROE\n3 List by ROA")

    @staticmethod
    def display_error():
        print("Invalid option!\n")

    @staticmethod
    def display_not_implemented():
        print("Not implemented!\n")

    @staticmethod
    def display_on_quit():
        print("Have a nice day!")

    @staticmethod
    def display_request():
        print("Enter an option:")


def main():
    while True:
        MenuDisplay.display_main()
        MenuDisplay.display_request()
        match input():
            case '0':
                MenuDisplay.display_on_quit()
                return
            case '1':
                MenuDisplay.display_crud()
                MenuDisplay.display_request()
                match input():
                    case '0':
                        continue
                    case '1' | '2' | '3' | '4' | '5':
                        MenuDisplay.display_not_implemented()
                    case _:
                        MenuDisplay.display_error()

            case '2':
                MenuDisplay.display_top_ten()
                MenuDisplay.display_request()
                match input():
                    case '0':
                        continue
                    case '1' | '2' | '3':
                        MenuDisplay.display_not_implemented()
                    case _:
                        MenuDisplay.display_error()
            case _:
                MenuDisplay.display_error()


if __name__ == '__main__':
    main()
