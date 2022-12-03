def main():
    total_number = int(input())
    accepted = int(input())
    list_of_candidates = iter(sorted([input().split(" ") for _ in range(total_number)],
                                     key=lambda x: (-float(x[2]), x[0] + x[1])))
    print("Successful applicants:")
    for _ in range(accepted):
        current = next(list_of_candidates)
        print(current[0], current[1])


if __name__ == '__main__':
    main()
