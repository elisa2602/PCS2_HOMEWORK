import requests
import re

def getFasta(file):
    proteins = []
    with open(file, "r") as f:
        for line in f:
            proteins.append(line.strip())
    
    prefix="https://www.uniprot.org/uniprot/"
    suffix=".fasta"
    
    FASTA = []
    for p in proteins:
        url = prefix+p.split("_")[0]+suffix
        all_fasta = requests.get(url).text
        split = all_fasta.split("\n")
        code = "".join(split[1:])
        FASTA.append((p, code))

    lookupMotif(FASTA)
    

def lookupMotif(fasta):
    pattern = r"(?=(N[^P][ST][^P]))"
    final = ""
    for f in fasta:
        code = f[1]
        motif = re.finditer(pattern, code)
        result = ""
        for found in motif:
            indexes = (found.start()+1)

            result += str(indexes)+" "
        result = result.strip()
        if result:
            final += f[0]+"\n"
            final += result+"\n"
        
    final = final.strip()
    
    with open("resultmprt.txt", "w") as f:
        f.write(final)
    
    return final

getFasta('rosalind_mprt (3).txt')