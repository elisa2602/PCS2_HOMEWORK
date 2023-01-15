def transit_transver_ratio(file):
    first = ""
    with open(file, "r") as f:
        second = ""
        for line in f:
            if line[0] == ">":
                if second:
                    first = second
                second = ""
                continue
            second += line.strip()
    
    purine = {"A","G"}
    pyramidine = {"C", "T"}
    
    transit = 0
    transver = 0
    for nuc_i in range(len(first)):
        nuc1 = first[nuc_i]
        nuc2 = second[nuc_i]
        if nuc1 != nuc2:
            if (nuc1 in purine and nuc2 in purine) or (nuc1 in pyramidine and nuc2 in pyramidine):
                transit += 1
            else:
                transver += 1
    
    score = transit/transver
    with open("resulttran.txt", "w") as f:
        f.write(f"{score:.11f}")
        
    return score

transit_transver_ratio('rosalind_tran.txt')