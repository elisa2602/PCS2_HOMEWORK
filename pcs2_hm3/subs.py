s = 'GTCAGCTATCAGCTACTTCAGCTACATCTTCAGCTAGGCCTGCTCAGCTAGGCTCAGCTACTTCAGCTATATACGATCAGCTAGTCAGCTAGAGGTTATCAGCTATCTACACTGTCAGCTAGATCAGCTAGTCAGCTATATGTCAGCTACTTCAGCTATCAGCTACATGTCACTCTGTGGTCAGCTAGTCAGCTACATCAGCTATCTCAGCTAGTACGGCAAGTCAGCTATTCAGCTACCTCAGCTAAGCATTCAGCTACGCCTCAGCTATCAGCTACATCAGCTATCAGCTAGTTCAGCTATCAGCTATCAGCTAACTCAGCTAATCAGCTAGCTATCAGCTAGTCAGCTATCAGCTATCAGCTAGGGTCAGCTACCTCAGCTACTATTGATCAGCTATCAGCTAGATATCAGCTAGGCTTCAGCTAGCTCAGCTACCCTCAGCTATCTCCCCGTCAGCTAGTCAGCTACGATCAGCTAAAATATTCAGCTATCAGCTATATCAGCTATGACTCAGCTAAGTGTGATTCAGCTAATTCAGCTAGGTCGTATTCAGCTATTCAGCTATCAGCTAGTCAGCTACTTAACACCTCAGCTAATCAGCTAAGTCAGCTAGCCAAAGTCAGCTACATCAGCTAGCTTAATATTGGTAGGGTCTGTGGGTCCTCAGCTAGTTCGAAGCACTCAGCTAACTCAGCTACATTCAGCTATCAGCTAAAGTCAGCTATCAGCTACATCACTCAGCTATACTCAGCTACGTTCAGCTACTAGTCAGCTACCTTCAGCTACTCAGCTAAATCAGCTACACTCAGCTATTCAGCTATCAGCTAATCTCAGCTAGTCAGCTATAAACAATGCATCAGCTATCAGCTATCAGCTATTCAGCTAACTCAGCTACTCAGCTAAGCCTCAGCTACCACGGTCAGCTACCCACCCATCAGCTATTCAGCTAGATCTCAGCTA'
t = 'TCAGCTATC'

loc = []
i = 0
j = 0

while i < len(s):
    j = s.find(t , i)
    if j > 0:
        i = j + 1
        loc.append(j + 1)
    else:
        i = i + 1

print(' '.join(map(str,loc)))