def main():
    to_do_list = ['Do yoga', 'Make a breakfast', 'Learn the basics of SQL', 'Learn about ORM']
    print("Today:")
    for inx, item in enumerate(to_do_list):
        print(f"{inx + 1}) {item}")


if __name__ == '__main__':
    main()
