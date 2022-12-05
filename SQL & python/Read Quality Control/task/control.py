from collections import Counter


def main():
    file_name = input()
    sequences = []
    with open(file_name, mode='r') as file:
        for ind, row in enumerate(file):
            if (ind - 1) % 4 != 0:
                continue
            sequences.append(len(row.strip()))
        with_counts = sorted(list(Counter(sequences).items()), key=lambda x: x[0])
        final_length = int(round(sum(sequences) / len(sequences), 0))
        print(f"Reads in the file = {len(sequences)}:")
        for k, v in with_counts:
            print(f"\twith length {k} = {v}")

        print(f"Reads sequence average length = {final_length}")


if __name__ == '__main__':
    main()
