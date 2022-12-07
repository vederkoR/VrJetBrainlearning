import gzip
from collections import Counter, namedtuple


def main():
    paths = [input() for _ in range(3)]
    Seq = namedtuple('Seq', 'seq_ln length gc_content n_content repet nuber_ns')
    seqs = []
    for path_to_file in paths:
        sequences = []
        with gzip.open(path_to_file, mode='r') as gz:
            file = gz.read().decode('utf8').split("\n")
            for ind, row in enumerate(file):
                if (ind - 1) % 4 != 0:
                    continue
                sequences.append(row.strip())

            final_length = int(round(sum([len(i) for i in sequences]) / len(sequences), 0))
            gc_content_avg = sum([(i.count('C') + i.count('G')) / len(i) for i in sequences]) / len(sequences)
            n_content_avg = sum([i.count('N') / len(i) for i in sequences]) / len(sequences)
            repetitions = sum([i[1] - 1 for i in Counter(sequences).items()])
            nuber_with_ns = len([i for i in sequences if 'N' in i])
            seqs.append(Seq(len(sequences), final_length, gc_content_avg, n_content_avg, repetitions, nuber_with_ns))

    seqs.sort(key=lambda x: x.nuber_ns)
    best_seq = seqs[0]

    print(f"Reads in the file = {best_seq.seq_ln}:")
    print(f"Reads sequence average length = {best_seq.length}")
    print()
    print("Repeats =", best_seq.repet)
    print("Reads with Ns =", best_seq.nuber_ns)
    print()
    print(f"GC content average = {best_seq.gc_content:.2%}")
    print(f"Ns per read sequence = {best_seq.n_content:.2%}")


if __name__ == '__main__':
    main()