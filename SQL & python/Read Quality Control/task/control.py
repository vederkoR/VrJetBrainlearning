import itertools
from collections import Counter


def main():
    path_to_file = input()
    sequences = []
    with open(path_to_file, mode='r') as file:
        for ind, row in enumerate(file):
            if (ind - 1) % 4 != 0:
                continue
            sequences.append(row.strip())
        # with_counts = sorted(list(Counter([len(i) for i in sequences]).items()), key=lambda x: x[0])
        # all_nucls = list(itertools.chain(*sequences))
        final_length = int(round(sum([len(i) for i in sequences]) / len(sequences), 0))
        gc_content_avg = sum([(i.count('C') + i.count('G')) / len(i) for i in sequences]) / len(sequences)
        n_content_avg = sum([i.count('N') / len(i) for i in sequences]) / len(sequences)
        repetitions = sum([i[1] - 1 for i in Counter(sequences).items()])
        nuber_with_ns = len([i for i in sequences if 'N' in i])
        print(f"Reads in the file = {len(sequences)}:")
        print(f"Reads sequence average length = {final_length}")
        print()
        print("Repeats =", repetitions)
        print("Reads with Ns =", nuber_with_ns)
        print()
        print(f"GC content average = {gc_content_avg:.2%}")
        print(f"Ns per read sequence = {n_content_avg:.2%}")


if __name__ == '__main__':
    main()
