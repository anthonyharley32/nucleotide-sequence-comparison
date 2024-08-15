import time
import pathlib
import readline

def print_amino_acid_library():


    print()
    print(f'{"Amino Acid Dictionary":^34}')
    print('-' * 36)
    print(f'{'Amino Acid Name':20}{'Code':^10}{'Codon':6}')
    print('-' * 36)
    print(f'{'Alanine':20}{'A':^10}{'GCA':6}')
    print(f'{'':20}{'':^10}{'GCC'}')
    print(f'{'':20}{'':^10}{'GCG'}')
    print(f'{'':20}{'':^10}{'GCT'}')
    print(f'{'Arginine':20}{'R':^10}{'AGA':6}')
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

def print_protein_library():
    print()
    file_path = pathlib.Path('seqs')
    num_proteins = len(list(file_path.iterdir()))
    print(f'Available Protein Count: {num_proteins}')
    print('-'*36)
    for protein in file_path.iterdir():
        print(protein.name)

def list_sequence(seq):
    for nucleotide in seq:
        print(nucleotide)

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
    
def analyze_sequence(seq):
    # Calculate the length of the sequence
    seq_length = len(seq)
    #count the number of A, T, G, and C
    a_count = seq.count('A')
    t_count = seq.count('T')
    g_count = seq.count('G')
    c_count = seq.count('C')
    # Count the occurrences of G and C
    gc_count = seq.count('G') + seq.count('C')
    
    # Calculate GC content as a percentage
    gc_content = (gc_count / seq_length) * 100
    
    # Print the results
    print()
    print('Sequence Analysis:')
    print(f"Sequence length: {seq_length} nucleotides")
    print(f"A count: {a_count}")
    print(f"T count: {t_count}")
    print(f"G count: {g_count}")
    print(f"C count: {c_count}")
    print(f"GC content: {gc_content:.2f}%")


def translate_sequence(seq, dict):
    if len(seq) % 3 != 0:
        print('Invalid sequence length.')
        return
    else:
        for i in range(0, len(seq), 3):
            codon = seq[i : i + 3]
            print(dict[codon][1], end='')

def lead():
    print('Loading.', end = '', flush = True)
    time.sleep(0.6)
    print('.', end = '', flush = True)
    time.sleep(0.3)
    print('.', end = '', flush = True)
    time.sleep(0.2)
    print(flush = True)

def file_set(num_vars):
    from prompt_toolkit import prompt
    from prompt_toolkit.completion import WordCompleter

    

    #path initialized
    file_path = pathlib.Path('seqs')

    #WordCompleter initialized
    available_files = [f.name for f in file_path.glob('*') if f.is_file()]
    file_completer = WordCompleter(available_files, ignore_case=True)

    #Determine file usage
    if num_vars == 1:
        while True:
            custom_file_bool = input('Run test file 1? (y/n)')
            if (custom_file_bool.lower() == 'y'):
                seq1 = read_sequence(file_path / 'test1.txt')
                return seq1
            elif (custom_file_bool.lower() == 'n'):
                print('Using custom file.')
                print()

                #custom file validation
                while True:
                    #autocomplete input
                    
                    file1 = prompt('Custom file: ', completer=file_completer)
                    #autocomplete input end
                    if (file_path / file1).exists():
                        seq1 = read_sequence(file_path / file1)
                        return seq1
                    else:
                        print('File does not exist.')
            else:
                print()
                print('Invalid entry. Try again.')
                print()
                
    elif num_vars == 2:
        while True:
            custom_file_bool = input('Run test files? (y/n)')
            if (custom_file_bool.lower() == 'y'):
                seq1 = read_sequence(file_path / 'test1.txt')
                seq2 = read_sequence(file_path / 'test2.txt')
                return seq1, seq2
            elif (custom_file_bool.lower() == 'n'):
                print('Using custom files.')
                print()

                #custom file validation
                while True:
                    file1 = prompt('Custom file 1: ', completer=file_completer)
                
                    if (file_path / file1).exists():
                        break
                    else:
                        print('File does not exist.')
                
                while True:
                    file2 = prompt('Custom file 2: ', completer=file_completer)
                    if (file_path / file2).exists():
                        break
                    else:
                        print('File does not exist.')
                
                seq1 = read_sequence(file_path / file1)
                seq2 = read_sequence(file_path/ file2)
                return seq1, seq2
            else:
                print()
                print('Invalid entry. Try again.')
                print()
    else:
        print('Call file_set() with 1 or 2 args.')
