def main():
    marks = [int(input()) for _ in range(3)]
    avg_score = sum(marks) / len(marks)
    print(avg_score)
    if avg_score < 60:
        print("We regret to inform you that we will not be able to offer you admission.")
    else:
        print("Congratulations, you are accepted!")


if __name__ == '__main__':
    main()