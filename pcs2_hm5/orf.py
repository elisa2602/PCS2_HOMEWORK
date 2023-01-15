def ORFS(file):
    translation_table = dict()
    with open("codons.txt", "r") as cod:
        for line in cod:
            strin, amin = line.split()
            translation_table[strin.replace("U","T")] = amin
    
    with open(file, "r") as f:
        f.readline()
        code = ""
        for line in f:
            code += line.strip()
            
    final = getORFs(translation_table, getReverseComplement(code))
    final += getORFs(translation_table, code)
    with open("resultORFS.txt", "w") as f:
        f.write("\n".join(list(set(final))))
        
def getReverseComplement(code):
    newCode = ""
    for c in code[::-1]:
        if c == "G":
            newCode+="C"
        elif c == "C":
            newCode+="G"
        elif c == "A":
            newCode+="T"
        elif c == "T":
            newCode+="A"
    return newCode

def getORFs(translation_table, code):
    index = code.find("ATG", 0)
    transl = ""
    final = []
    while (index != -1):
        transl += "M"
        i = index+3
        stopped = False
        for j in range(i,len(code)-2,3):
            tri = code[j:j+3]
            trans = translation_table[tri]
            if trans == "Stop":
                stopped = True
                break
            transl+=trans
        
        if stopped:
            final.append(transl)
            
        transl = ""
        index = code.find("ATG", index+1)

    return final

ORFS('rosalind_orf.txt')