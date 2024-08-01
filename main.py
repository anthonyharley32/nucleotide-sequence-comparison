#Python DNA Test
import time 
import dna_utils


#TODOS
#Define a test function to test a file for having valid input
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



def main():

    #Set files
    seq1, seq2 = dna_utils.file_set()

    #Translate Sequence 
    dna_utils.translate_sequence(seq1, codon_code_dictionary)


    dna_utils.print_sequence_comparison(seq1, seq2)

    dna_utils.load()

    #Print Amino Acid Dictionary for user
    dna_utils.print_amino_acid_library()
    


    









if __name__ == '__main__':
    main()