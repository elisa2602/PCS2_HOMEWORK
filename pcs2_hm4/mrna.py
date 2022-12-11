def mrna(protein):
    codons_table = {'F': ['UUU', 'UUC'], 'L': ['UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG'], 'S': ['UCU', 'UCC', 'UCA', 'UCG', 'AGU', 'AGC'], 'Y': ['UAU', 'UAC'], 'Stop': ['UAA', 'UAG', 'UGA'], 'C': ['UGU', 'UGC'], 'W': ['UGG'], 'P': ['CCU', 'CCC', 'CCA', 'CCG'], 'H': ['CAU', 'CAC'], 'Q': ['CAA', 'CAG'], 'R': ['CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'], 'V': ['GUU', 'GUC', 'GUA', 'GUG'], 'A': ['GCU', 'GCC', 'GCA', 'GCG'], 'D': ['GAU', 'GAC'], 'E': ['GAA', 'GAG'], 'G': ['GGU', 'GGC', 'GGA', 'GGG'], 'I': ['AUU', 'AUC', 'AUA'], 'M': ['AUG'], 'T': ['ACU', 'ACC', 'ACA', 'ACG'], 'N': ['AAU', 'AAC'], 'K': ['AAA', 'AAG']}
    count = 1
    for i in protein:
        count = count *len(codons_table[i])
    count = count*len(codons_table['Stop'])
    return count % 1000000

if __name__ == '__main__':
    with open("C:\\Users\\Asus\\Desktop\\bioinformatics\\2\\1\\principles of computer science 2\\cs2\\pcs2_hm\\pcs2_hm4\\rosalind_mrna (2).txt") as f:                         
        protein = f.readline().strip()     
        count = mrna(protein)
        print(count)