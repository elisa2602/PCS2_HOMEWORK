def search_subsequence(file):
    first = ""
    with open(file, "r") as f:
        sub = ""
        for line in f:
            if line[0] == ">":
                if sub:
                    first = sub
                sub = ""
                continue
            sub += line.strip()
    
    index = 0
    indeces = list()
    for nuc_i in range(len(first)):
        if first[nuc_i] == sub[index]:
            indeces.append(str(nuc_i+1))
            index+=1
        if index == len(sub):
            break
    
    with open("resultsseq.txt", "w") as f:
        f.write(" ".join(indeces))

search_subsequence('rosalind_sseq.txt')