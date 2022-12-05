def main():
    file_name = input()
    with open(file_name, mode='r') as file:
        for ind, row in enumerate(file):
            print(row.strip())
            if ind == 3:
                break


if __name__ == '__main__':
    main()
