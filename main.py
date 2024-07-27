#Python DNA Test
import time 
import dna_utils


#TODOS
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
            seq1 = dna_utils.read_sequence('test1.txt')
            seq2 = dna_utils.read_sequence('test2.txt')
            repeat = False

        elif (custom_file_bool.lower() == 'n'):
            print('Using custom files.')
            print()

            file1 = input('Custome file 1: ')
            file2 = input('Custome file 2: ')

            seq1 = dna_utils.read_sequence(file1)
            seq2 = dna_utils.read_sequence(file2)
            repeat = False

        else:
            print()
            print('Invalid entry. Try again.')
            print()
            


    #Pad and print string information and match percentage
    print()
    print(f'Original lengths: {len(seq1)}, {len(seq2)}')

    seq1_padded, seq2_padded = dna_utils.pad_sequence(seq1, seq2)

    print(f'Padded lengths: {len(seq1_padded)}, {len(seq2_padded)}')

    total_chars, matches = dna_utils.compare_sequence(seq1_padded, seq2_padded)

    print(f"Total characters: {total_chars}")
    print(f"Matching characters: {matches}")
    print(f"Match percentage: {matches / total_chars * 100:.2f}%")
    print()
    input('Press Enter to load Amino Acid Dictionary...')
    print()

    #Loading "Graphic"
    print('Loading.', end = '', flush = True)
    time.sleep(0.5)
    print('.', end = '', flush = True)
    time.sleep(0.5)
    print('.', end = '', flush = True)
    time.sleep(0.5)
    print(flush = True)

    #Print Amino Acid Dictionary for user
    dna_utils.print_amino_acid_library()
    

    print()
    print() 

    









if __name__ == '__main__':
    main()