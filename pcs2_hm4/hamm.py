s ='CTTCGGATAAACTACTCAGATATGCATCGATCTGTATTCAGCAAAAGCGTGATTTGAGGACTATGGCGGAAGAGCAACGAAGACCCTTTCACGTCACATTAAAGTACGCAAACGAGTCGTCCGGGATGAATTCTGACCCTACGCATCGCATCATTCATGTCATGCAGATTGTGTTTAGTCACCTTACGACTGGAGCGGATCAGGAGTGTAGCCTCTGCTGATACACCCGAACGTCCCTGAAAGGATTACCGTGTCTTGGCCAAAACACAATAACACGAAACTTTATCATCCGCGTGGAGCATGTAAGCATTCGCATTATGTGTTTGTGAGTAGAAGTGTGATCGGTTAGGTGGTGGAGTACTGGCTTTAAACACGATTTCCGTTATGATCCGACTGGAGTTGTTAGTTTGAGCCGAAGACTTAATGGGCTAGCAGGGGCCTTCCTCTCGAAGGCCTCCCACAACAACGGTCGTGAAAAGCATTGGTGCAAGGGCATAAGATATTCTCCCCACATCTCCGATGAGGATTGACAAGAAGATTTAAGCGCACGGCCTTGACTGGTTCACACGACCTACTCTCACATCGGCGACACTCATATCGACTCGTGGTACGGTCCTCCCATCGTAGCGCATATCACCTAATGCAAACGCTGCTGCTCTTTAAAATTTTCGAGGCTGGAACAGACGCGGACTACCACTTTTTTAAAGACCAGCGCGATATCGCTAGGTGTAAAATCGAAGTAGCGTGGGTTGTGAGCCGCTTTCGCCTACGGGGACTATTAACGTCAAAAGCTGGTGTCAACTGGCCGACTTATGATTTTGAGACAAAATGCCGATAGCGTTCCCGCAGGTGGAGGCTTCAAAAGGCGAGGATCTCGAAAGAGGTTGCTCTTGGATATGAGCACACTATATGTTATCCGATCAACGG'
t ='TGCCATAAAAAATGCTGAGATACGCGTCCATCCTAACGAAGCGATAGTGTGACGTGTGGACGAAGGCGGAGAAGGAACCAAGCCCCACGCCCATCATGTCTAAGTCGCCATACTACTCCTCAAGTAGGGCCCGTTCACCTGCCTGATTGTAATTACAGGGAATCGAGTTGACGTCGCTCCTCCTTAGGAGAAAAGCGTACCGGGTCAGACTCCTCGGCGGAGGCACCTCCACGGCGGTGCATGCATGACCGTGAAATTTCGGCACAACAATAGGCGGAAAAATTCACGATCAAGGACAACACTAATTCACATGTAGTGTGTATTTTGGACCTGACCTGGCAGTGGTTAGGTGTTGTAGTTCTCGCCTGAAGTACTTTGAAGGTCATACGGTATCTATAGTTCTGGGTCAGAGTCGCTGATATATTGCCCGAGTATATGCACGCCCCACTAATTTTGCAGTTCTAGAAATTAGTCCAAGGCTATCTGCTAGCGGACTAATATACTCTACTCACATCCCCGGAGCGGGGTTGCGAGTTTATCTTAACGAACTGCCCTCCAGAGTGCCCATACTCGACTTTCCGAAAGGCAACGCGCATATCGTCTGGTGGTTGGATTTAGCCATCGTAGTCTCTCCCCCCTAAAGGAAACGGCGCTATTCTTAACCCTTCAAAAAGCCGGTAGAGAACCGAGCAACTACCTTCTTTATGAGCAATCTGAAAATGACACCTTTAACGCGGAAGCAGCATTCGTTGTCAGGCGTTTCCGAACACGGGAATAATTACCATCAAAAGGCCAGGGACGAGAACTGACGTAGTGTTTTTGTGCAACATTACAATCCACTTCCTCCTGGTGGACGCTGCAAAATACCCTAGTCTCGCTACAAGAGACGAGTGGATATGCGCTCATCTTATGTAACAAGCTCAGCGA'
count = 0
hamm = 0

while count < len(s):
    if s[count] != t[count]:
        hamm += 1
    count += 1

print(hamm)
    