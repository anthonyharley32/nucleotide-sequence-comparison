#Python DNA Test
import time 
import dna_utils


#TODOS
#Define a test function to test a file for having valid input
#fix file set for having there be a valid file when using custom file
#Use dictionary to make cases to navigate program functionality
#Build a searchable database of polypeptides and their amino acid sequences



#Define a dictionary for all codon/amino acid pairs
#add a nucleotide count functionality

codon_code_dictionary = {
    'AAA': ('Lysine', 'K'),
    'AAC': ('Asparagine', 'N'),
    'AAG': ('Lysine', 'K'),
    'AAT': ('Asparagine', 'N'),
    'ACA': ('Threonine', 'T'),
    'ACC': ('Threonine', 'T'),
    'ACG': ('Threonine', 'T'),
    'ACT': ('Threonine', 'T'),
    'AGA': ('Arginine', 'R'),
    'AGC': ('Serine', 'S'),
    'AGG': ('Arginine', 'R'),
    'AGT': ('Serine', 'S'),
    'ATA': ('Isoleucine', 'I'),
    'ATC': ('Isoleucine', 'I'),
    'ATG': ('Methionine', 'M'),
    'ATT': ('Isoleucine', 'I'),
    'CAA': ('Glutamine', 'Q'),
    'CAC': ('Histidine', 'H'),
    'CAG': ('Glutamine', 'Q'),
    'CAT': ('Histidine', 'H'),
    'CCA': ('Proline', 'P'),
    'CCC': ('Proline', 'P'),
    'CCG': ('Proline', 'P'),
    'CCT': ('Proline', 'P'),
    'CGA': ('Arginine', 'R'),
    'CGC': ('Arginine', 'R'),
    'CGG': ('Arginine', 'R'),
    'CGT': ('Arginine', 'R'),
    'CTA': ('Leucine', 'L'),
    'CTC': ('Leucine', 'L'),
    'CTG': ('Leucine', 'L'),
    'CTT': ('Leucine', 'L'),
    'GAA': ('Glutamic acid', 'E'),
    'GAC': ('Aspartic acid', 'D'),
    'GAG': ('Glutamic acid', 'E'),
    'GAT': ('Aspartic acid', 'D'),
    'GCA': ('Alanine', 'A'),
    'GCC': ('Alanine', 'A'),
    'GCG': ('Alanine', 'A'),
    'GCT': ('Alanine', 'A'),
    'GGA': ('Glycine', 'G'),
    'GGC': ('Glycine', 'G'),
    'GGG': ('Glycine', 'G'),
    'GGT': ('Glycine', 'G'),
    'GTA': ('Valine', 'V'),
    'GTC': ('Valine', 'V'),
    'GTG': ('Valine', 'V'),
    'GTT': ('Valine', 'V'),
    'TAA': ('Stop', '*'),
    'TAC': ('Tyrosine', 'Y'),
    'TAG': ('Stop', '*'),
    'TAT': ('Tyrosine', 'Y'),
    'TCA': ('Serine', 'S'),
    'TCC': ('Serine', 'S'),
    'TCG': ('Serine', 'S'),
    'TCT': ('Serine', 'S'),
    'TGA': ('Stop', '*'),
    'TGC': ('Cysteine', 'C'),
    'TGG': ('Tryptophan', 'W'),
    'TGT': ('Cysteine', 'C'),
    'TTA': ('Leucine', 'L'),
    'TTC': ('Phenylalanine', 'F'),
    'TTG': ('Leucine', 'L'),
    'TTT': ('Phenylalanine', 'F')
}

class Menu:
   
    def __init__(self):
        self.menus = {
            'main' : {
                '1' : 'Print Amino Acid Library',
                '2' : 'Print Accessible Proteins',
                '3' : 'Translate DNA Sequence',
                '4' : 'Compare DNA Sequences',
                '0' : 'Exit'
            }

        }

        self.actions = {
            'main' : {
                '1' : self.print_library,
                '2' : self.print_proteins,
                '3' : self.translate_sequence,
                '4' : self.compare_sequences,
                '0' : self.exit
            }
        }

        self.current_menu = 'main'

    def display_menu(self):
       print(f'{self.current_menu.capitalize()} Menu:')
       for options, description in self.menus[self.current_menu].items():
          print(f'{options}. {description}')

    def handle_input(self, user_input):
        if user_input in self.menus[self.current_menu]:
          self.actions[self.current_menu][user_input]()
        else:
           print()
           print('--Invalid input. Please try again.--')
           print()

    def print_library(self):
        dna_utils.print_amino_acid_library()

    def print_proteins(self):
        dna_utils.print_protein_library()

    def translate_sequence(self):
        seq = dna_utils.file_set(1)
        dna_utils.translate_sequence(seq, codon_code_dictionary)
        print()


    def compare_sequences(self):
        seq1, seq2 = dna_utils.file_set(2)
        #Pad and print string information and match percentage
        print()
        print(f'Original lengths: {len(seq1)}, {len(seq2)}')
        seq1_padded, seq2_padded = dna_utils.pad_sequence(seq1, seq2)
        print(f'Padded lengths: {len(seq1_padded)}, {len(seq2_padded)}')
        total_chars, matches = dna_utils.compare_sequence(seq1_padded, seq2_padded)
        print(f"Total characters: {total_chars}")
        print(f"Matching characters: {matches}")
        print(f"Match percentage: {matches / total_chars * 100:.2f}%")


    def exit(self):
        print('Goodbye', end = '')
        for i in range(3):
            time.sleep(.5)
            print('.', end = '')
        exit()
       




def main():

    #Main Menu
    #1) Translate DNA Sequence: Translate a DNA sequence into amino acids.
    #2) Compare DNA Sequences: Compare two DNA sequences for similarities.
    #3) Search Amino Acid Database: Search for specific amino acids or polypeptides.
    #4) Load Custom DNA Sequence: Load a custom DNA sequence from a file.
    #0) Exit: Quit the program.

    menu = Menu()

    while True:
       print()
       menu.display_menu()
       user_input = input('Enter an option: ')
       menu.handle_input(user_input)
   


if __name__ == '__main__':
    main()