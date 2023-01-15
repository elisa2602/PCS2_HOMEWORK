def splice(file):
    translation_table = dict()
    with open("codons.txt", "r") as cod:
        for line in cod:
            strin, amin = line.split()
            translation_table[strin.replace("U","T")] = amin
        
    substrings = []
    
    with open(file, "r") as f:
        sub = ""
        for line in f:
            if line[0] == ">":
                if sub:
                    substrings.append(sub)
                sub = ""
                continue
            sub+=line.strip()
        substrings.append(sub)
        
        code = substrings[0]
        substrings = substrings[1:]
        
    res = code
    for subs in substrings:
        res = res.replace(subs, "")
        
    final = ""
    for i in range(0, len(res), 3):
        tri = res[i:i+3]
        trans = translation_table[tri]
        if trans == "Stop":
            break    
        final+=trans
        
    with open("resultsplc.txt", "w") as f:
        f.write(final)

splice('rosalind_splc (1).txt')