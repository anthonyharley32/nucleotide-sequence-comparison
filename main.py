#Python DNA Test

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

#Define a test function to test a file for having valid input
#Define a dictionary for all codon/amino acid pairs



def main():
    file1 = 'test1.txt'
    file2 = 'test2.txt'
    repeat = True

    #Declare files to use for nucleotide comparison

    while repeat == True:
        custom_file_bool = input('Run test files? (Y/N)')
        
    
        if (custom_file_bool.lower() == 'y'):
            seq1 = read_sequence('test1.txt')
            seq2 = read_sequence('test2.txt')
            repeat = False

        elif (custom_file_bool.lower() == 'n'):
            print('Using custom files.')
            print()

            file1 = input('Custome file 1: ')
            file2 = input('Custome file 2: ')

            seq1 = read_sequence(file1)
            seq2 = read_sequence(file2)
            repeat = False

        else:
            print()
            print('Invalid entry. Try again.')
            print()
            


    #Pad and print string information and match percentage
    print()
    print(f'Original lengths: {len(seq1)}, {len(seq2)}')

    seq1_padded, seq2_padded = pad_sequence(seq1, seq2)

    print(f'Padded lengths: {len(seq1_padded)}, {len(seq2_padded)}')

    total_chars, matches = compare_sequence(seq1_padded, seq2_padded)

    print(f"Total characters: {total_chars}")
    print(f"Matching characters: {matches}")
    print(f"Match percentage: {matches / total_chars * 100:.2f}%")
    print()
    input('Press Enter to continue...')
    print()
    #Print Amino Acid Dictionary for user

    print(f'{"Amino Acid Dictionary":^34}')
    print('-' * 36)
    print(f'{'Amino Acid Name':20}{'Code':^10}{'Codon':6}')
    print('-' * 36)
    print(f'{'Alanine':20}{'A':^10}{'GCA':6}')
    print(f'{'':20}{'':^10}{'GCC'}')
    print(f'{'':20}{'':^10}{'GCG'}')
    print(f'{'':20}{'':^10}{'GCT'}')
    print(f'{'Arginine':20}{'N':^10}{'AGA':6}')
    print(f'{'':20}{'':^10}{'AGG'}')
    print(f'{'':20}{'':^10}{'CGA'}')
    print(f'{'':20}{'':^10}{'CGC'}')
    print(f'{'':20}{'':^10}{'CGG'}')
    print(f'{'':20}{'':^10}{'CGT'}')
    print(f'{'Asparagine':20}{'N':^10}{'AAC':6}')
    print(f'{'':20}{'':^10}{'AAT'}')
    print(f'{'Aspartic Acid':20}{'D':^10}{'GAC':6}')
    print(f'{'':20}{'':^10}{'GAT'}')
    print(f'{'Cysteine':20}{'C':^10}{'TGC':6}')
    print(f'{'':20}{'':^10}{'TGT'}')
    print(f'{'Glutamic Acid':20}{'E':^10}{'GAA':6}')
    print(f'{'':20}{'':^10}{'GAG'}')
    print(f'{'Glutamine':20}{'Q':^10}{'CAA':6}')
    print(f'{'':20}{'':^10}{'CAG'}')
    print(f'{'Glycine':20}{'G':^10}{'GGA':6}')
    print(f'{'':20}{'':^10}{'GGC'}')
    print(f'{'':20}{'':^10}{'GGG'}')
    print(f'{'':20}{'':^10}{'GGT'}')
    print(f'{'Histidine':20}{'H':^10}{'CAC':6}')
    print(f'{'':20}{'':^10}{'CAT':6}')
    print(f'{'Isoleucine':20}{'I':^10}{'ATA':6}')
    print(f'{'':20}{'':^10}{'ATC':6}')
    print(f'{'':20}{'':^10}{'ATT':6}')
    print(f'{'Leucine':20}{'L':^10}{'CTA':6}')
    print(f'{'':20}{'':^10}{'CTC':6}')
    print(f'{'':20}{'':^10}{'CTG':6}')
    print(f'{'':20}{'':^10}{'CTT':6}')
    print(f'{'':20}{'':^10}{'TTA':6}')
    print(f'{'':20}{'':^10}{'TTG':6}')
    print(f'{'Lysine':20}{'K':^10}{'AAA':6}')
    print(f'{'':20}{'':^10}{'AAG':6}')
    print(f'{'Methionine':20}{'M':^10}{'ATG':6}')
    print(f'{'Phenylalanine':20}{'F':^10}{'TTC':6}')
    print(f'{'':20}{'':^10}{'TTT':6}')
    print(f'{'Proline':20}{'P':^10}{'CCA':6}')
    print(f'{'':20}{'':^10}{'CCC':6}')
    print(f'{'':20}{'':^10}{'CCG':6}')
    print(f'{'':20}{'':^10}{'CCT':6}')
    print(f'{'Serine':20}{'S':^10}{'AGC':6}')
    print(f'{'':20}{'':^10}{'AGT':6}')
    print(f'{'':20}{'':^10}{'TCA':6}')
    print(f'{'':20}{'':^10}{'TCC':6}')
    print(f'{'':20}{'':^10}{'TCG':6}')
    print(f'{'':20}{'':^10}{'TCT':6}')
    print(f'{'Threonine':20}{'T':^10}{'ACA':6}')
    print(f'{'':20}{'':^10}{'ACC':6}')
    print(f'{'':20}{'':^10}{'ACG':6}')
    print(f'{'':20}{'':^10}{'ACT':6}')
    print(f'{'Tryptophan':20}{'W':^10}{'TGG':6}')
    print(f'{'Tyrosine':20}{'Y':^10}{'TAC':6}')
    print(f'{'':20}{'':^10}{'TAT':6}')
    print(f'{'Valine':20}{'V':^10}{'GTA':6}')
    print(f'{'':20}{'':^10}{'GTC':6}')
    print(f'{'':20}{'':^10}{'GTG':6}')
    print(f'{'':20}{'':^10}{'GTT':6}')
    print(f'{'Stop':20}{'*':^10}{'TAA':6}')
    print(f'{'':20}{'':^10}{'TAG':6}')
    print(f'{'':20}{'':^10}{'TGA':6}')

    









if __name__ == '__main__':
    main()