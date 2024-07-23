def read_sequence(filename):
    with open(filename, 'r') as file:
        return file.read().strip()

def pad_sequence(seq1, seq2):
    max_length = max(len(seq1), len(seq2))
    return seq1.ljust(max_length, '-'), seq2.ljust(max_length, '-')

def compare_sequence(seq1, seq2):
    total_chars = len(seq1)
    matches = sum(1 for a, b in zip(seq1, seq2) if a == b)
    return total_chars, matches

def main():
    file1 = 'test1.txt'
    file2 = 'test2'

    seq1 = read_sequence('test1.txt')
    seq2 = read_sequence('test2.txt')

    print(f'Original lengths: {len(seq1)}, {len(seq2)}')

    seq1_padded, seq2_padded = pad_sequence(seq1, seq2)

    print(f'Padded lengths: {len(seq1_padded)}, {len(seq2_padded)}')

    total_chars, matches = compare_sequence(seq1_padded, seq2_padded)

    print(f"Total characters: {total_chars}")
    print(f"Matching characters: {matches}")
    print(f"Match percentage: {matches / total_chars * 100:.2f}%")


if __name__ == '__main__':
    main()