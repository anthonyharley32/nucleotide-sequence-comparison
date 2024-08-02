#Python DNA Test
import time 
import dna_utils


#TODOS
#Define a test function to test a file for having valid input
#fix file set for having there be a valid file when using custom file
#Use dictionary to make cases to navigate program functionality
#Build a searchable database of polypeptides and their amino acid sequences



#Define a dictionary for all codon/amino acid pairs


codon_code_dictionary = {
    'AAA' :  'Lysine',
    'AAC' : 'Asparagine',
    'AAG' : 'Lysine',
    'AAT' : 'Asparagine',
    'ACA' : 'Threonine',
    'ACC' : 'Threonine',
    'ACG' : 'Threonine',
    'ACT' : 'Threonine',
    'AGA' : 'Arginine',
    'AGC' : 'Serine',
    'AGG' : 'Arginine',
    'AGT' : 'Serine',
    'ATA' : 'Isoleucine',
    'ATC' : 'Isoleucine',
    'ATG' : 'Methionine (Start Codon)',
    'ATT' : 'Isoleucine',
    'CAA' : 'Glutamine',
    'CAC' : 'Histidine',
    'CAG' : 'Glutamine',
    'CAT' : 'Histidine',
    'CCA' : 'Proline',
    'CCC' : 'Proline',
    'CCG' : 'Proline',
    'CCT' : 'Proline',
    'CGA' : 'Arginine',
    'CGC' : 'Arginine',
    'CGG' : 'Arginine',
    'CGT' : 'Arginine',
    'CTA' : 'Leucine',
    'CTC' : 'Leucine',
    'CTG' : 'Leucine',
    'CTT' : 'Leucine',
    'GAA' : 'Glutamic acid',
    'GAC' : 'Aspartic acid',
    'GAG' : 'Glutamic acid',
    'GAT' : 'Aspartic acid',
    'GCA' : 'Alanine',
    'GCC' : 'Alanine',
    'GCG' : 'Alanine',
    'GCT' : 'Alanine',
    'GGA' : 'Glycine',
    'GGC' : 'Glycine',
    'GGG' : 'Glycine',
    'GGT' : 'Glycine',
    'GTA' : 'Valine',
    'GTC' : 'Valine',
    'GTG' : 'Valine',
    'GTT' : 'Valine',
    'TAA' : 'Stop codon',
    'TAC' : 'Tyrosine',
    'TAG' : 'Stop codon',
    'TAT' : 'Tyrosine',
    'TCA' : 'Serine',
    'TCC' : 'Serine',
    'TCG' : 'Serine',
    'TCT' : 'Serine',
    'TGA' : 'Stop codon',
    'TGC' : 'Cysteine',
    'TGG' : 'Tryptophan',
    'TGT' : 'Cysteine',
    'TTA' : 'Leucine',
    'TTC' : 'Phenylalanine',
    'TTG' : 'Leucine',
    'TTT' : 'Phenylalanine'
}

class Menu:
   
    def __init__(self):
        self.menus = {
            'main' : {
                '1' : 'Print Amino Acid Library',
                '2' : 'Translate DNA Sequence',
                '3' : 'Compare DNA Sequences',
                '0' : 'Exit'
            }
        }

        self.actions = {
            'main' : {
                '1' : self.print_library,
                '2' : self.translate_sequence,
                '3' : self.compare_sequences,
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
           print('Invalid input. Please try again.')

    def print_library(self):
        dna_utils.print_amino_acid_library()

    #FIX_ME
    def translate_sequence(self):    
        pass

    #FIX_ME
    def compare_sequences(self):
        dna_utils.compare_sequence()

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

    #Set files - FIRMWARE
    seq1, seq2 = dna_utils.file_set()
    print()

    menu = Menu()

    while True:
       menu.display_menu()
       user_input = input('Enter an option: ')
       menu.handle_input(user_input)
   


if __name__ == '__main__':
    main()