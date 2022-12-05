import itertools
from collections import Counter


def main():
    file_name = input()
    sequences = []
    with open(file_name, mode='r') as file:
        for ind, row in enumerate(file):
            if (ind - 1) % 4 != 0:
                continue
            sequences.append(row.strip())
        # with_counts = sorted(list(Counter([len(i) for i in sequences]).items()), key=lambda x: x[0])
        all_nucls = list(itertools.chain(*sequences))
        final_length = int(round(sum([len(i) for i in sequences]) / len(sequences), 0))
        gc_contant_avg = sum([(i.count('C') + i.count('G')) / len(i) for i in sequences]) / len(sequences)
        print(f"Reads in the file = {len(sequences)}:")
        print(f"Reads sequence average length = {final_length}")
        print()
        print(f"GC content average = {gc_contant_avg:.2%}")


if __name__ == '__main__':
    main()
