#first option

s = 'TTCTGCTAGCTAGGTAGTCGCCGGACATTAATTGCTTTACGGTGAAAAGAATGGTGTGTCGCTAGGTTCCGTCTGTATTGATATCAAACACGAATCTCGTTTAGAACTGCGAGCAATACATCTACGGCGGACGCGCTTACTGGGAGATGCGTAGCAAGTACCAGCGGCCCCAATGATCAACGGAGGTACGCTGTAAGACCCGTTCACAGACCCCTCGTGCTGGGGAGAAGGGGGCACTTGACCCGAATCAGCCATGTTAGGGCCGCTGGAAGACGAGGCTTAGCATCCACTTAATAGAGCGTTCTAAACGACCACCCCACGACCACTCGGCTGACGGAGAAGACAAAGGTCAAACTGGGTTTTTAACAGGATAAAACGACTAATCCATCTGGTAATTGGCCGAGGCAGAGAGGTGGATGCCCTCGTCCAACACGATAACCGGGCCCAGCCAATAATTCCTCCTAATACAGAGGGAGCCTTCAAATGCTCGGGACAGATGATACTTCAGTGGTAGGCCCGATCTCGAGATTTCGAGTTTCGTACAAATTGCGCACATCAAGTAGCCGTTCTACAGGATTATCCACCTAGAATGCGATCGTTCTAATGGCTGGCGAAACTCGAAAGATCGGTTGCTTGTTTCAACTTCCGGCTCCCGGAATGTGAGCAAGGTACTCAACTTCCCTTCGTATCAGGCGGATAGTTTGCGGGCTCTGCTATCAGACTTCTCCGTAAGGGTCGGACGAGGACCTAACATCAGCCGCGAGATGCTTTTAACGTTACCCCGCTCGGTAGCAGATCACCCCGGTATATGTGAGTATTCGCCTTCGGGTCGAAACGACTGTGGACTACGCCGCTGTGGTCTACTTGGC'

nucleotides_repl = {'A':'T','T':'A','C':'G','G':'C'}

s_1 = s.translate(s.maketrans(nucleotides_repl))

print(s_1[::-1])


#second option

with open('rosalind_revc (3).txt', 'r') as file:
    s = file.read().replace('\n', '')

nucleotides_repl = {'A':'T','T':'A','C':'G','G':'C'}

s_1 = s.translate(s.maketrans(nucleotides_repl))

print(s_1[::-1])
