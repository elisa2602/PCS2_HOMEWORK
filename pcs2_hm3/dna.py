# first option
from collections import Counter

s = 'GTGAAGGTGTACGGATCAGAGCATGTTTCTTGGACATATTCTTACAATAAACACCGATACGAAACCGTTATATCGCGCTGTGGATCTCATAGGTGAAAAGTGAACAGGCTGTTGACGGTGGCATTCATTCGTGATGGACAGGAATGAGCAAAGGATTGTACGCCCTCAGGTCCTCCTTAATATAGAAACTACTGACGTACAGGCTATCGTTGCCTATAAGAGGCGATCCATTTGATGTTAGTTGGAACATATATCTGACAAGCAGAACGGGCCGGTTGACTCGTTCGTAGACCCTGCCCCGTGGCCTATCCTGAATGTCCAGTTGCCTGGCGTCAAATTTCGGAGAAAGGCTCACAGCATTCAGAGCCCGTAACGACAGACTCTCCGCGGAACGAATGTCTAATGTGACTGTCAAGTTGAACGTCTGACGTGTAAATACACTCGGCCACGTCTAGACGGACGGCACACTTTCATAATTCTTAGGAGCTCGCGAGCCCTAGTAAAGTATCAATGCGGCACATTATTGGACTACGGCCTTATGTGCGGGTAGTGCTGCAGCGTCCTTAGACTTCCGGACTTATTAGTTGATTTCCCGCCCGTAAATTAATTGCCCAAAAGTGCATAGAACAGAGGCTAAACAGCTCGTGACGCCTCCCGGAGGAATACAACTACACGTAACTTAGACTCTCGGAGCACGAGTCGATGTACCTGCAAAGGGGATCTTGGTATTAGGCGCACGATAAGTGGAATTGTGGATAATATGGGGAAGGCACCCTCATATGTATGTGACCGAGGAATTCTCACCGAACCCCTTAAGGGCGTCAGGGGAACCTACTGG'

dna_seq = Counter(s)

print(dna_seq['A'], dna_seq['C'], dna_seq['G'], dna_seq['T'])

# second option
from collections import Counter

with open('rosalind_dna (1).txt', 'r') as file:
    s = file.read().replace('\n', '')

dna_seq = Counter(s)

print(dna_seq['A'],dna_seq['C'],dna_seq['G'],dna_seq['T'])