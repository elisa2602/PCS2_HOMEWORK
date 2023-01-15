def prefix_suffix(file):
    with open(file, "r") as f:
        identifier = ""
        code = ""
        codes = []
        for r in f:
            if r[0] == '>':
                if identifier != "":
                    codes.append((identifier.strip(), code))
                code = ""
                identifier = r[1:]
            else:
                code += r.strip()
        codes.append((identifier.strip(), code))
    
    link = []
    k = 3
    for x in range(0, len(codes)):
        for y in range(0, len(codes)):
            if x == y:
                continue
            if codes[x][1][-k:] == codes[y][1][:k]:
                link.append(codes[x][0] + " " + codes[y][0])
    
    
    with open("resultgrph.txt","w") as f:
        for l in link:
           f.write(l)
           f.write("\n")
    
    return link
    
prefix_suffix('rosalind_grph (3).txt')