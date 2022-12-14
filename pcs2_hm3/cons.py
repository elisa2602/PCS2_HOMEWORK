def Consensus(DNAs):
    profile = []
    for i in range(len(DNAs[0])):
        A,C,T,G = 0, 0, 0, 0
        for j in range(len(DNAs)):
            if DNAs[j][i] == 'A':
                A += 1
            elif DNAs[j][i] == 'C':
                C += 1
            elif DNAs[j][i] == 'T':
                T += 1
            elif DNAs[j][i] == 'G':
                G += 1
        profile.append([[A,'A'],[C,'C'],[G,'G'],[T,'T']])

    consensus = ''
    for row in profile:
        common = max(row)
        consensus += common[1]
    print(consensus)
    for i in range(4):
        record = profile[0][i][1] + ': '
        for j in range(len(profile)):
            record += str(profile[j][i][0]) + ' '
        print(record)



with open("C:\\Users\\Asus\\Desktop\\bb2\\cs2\\pcs2_hm\\pcs2_hm3\\rosalind_cons (5).txt",'r') as file:
    content = file.read()
DNAs_number, lines, line_number, DNAs = content.count('>'), content.splitlines(), 0, []
for i in range(DNAs_number):
    DNA = ''
    line_number += 1
    while lines[line_number][0] != '>':
        DNA += lines[line_number]
        line_number += 1
        if line_number+1 > len(lines):
            break
    DNAs.append(DNA)

Consensus(DNAs)
