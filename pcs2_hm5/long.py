def long(file):
    sequences = []
    with open(file, "r") as f:
        code = ""
        for line in f:
            if line[0] == ">":
                if code:
                    sequences.append(code)
                code = ""                
                continue
            code+=line.strip()
        sequences.append(code)
    
    
    index = 0
    i = 1
    while len(sequences) > 1:
        seq1 = sequences[index]
        while i < len(sequences):
            if i == index:
                i+=1
                continue
            seq2 = sequences[i]
            res1 = overlap(seq1, seq2)
            res2 = overlap(seq2, seq1)
            if res1:
                sequences[index] = res1
                sequences = sequences[:i] + sequences[i+1:]
                i = 0
                index -= 1
                break
            elif res2:                
                sequences[index] = res2
                sequences = sequences[:i] + sequences[i+1:]
                i = 0
                index -= 1
                break
            i += 1
        
        if index > len(sequences):
            index = 0
        else:
            index += 1 
    
    with open("resultlong.txt", "w") as f:
        f.write(sequences[0])
    
    return sequences[0]
    
def overlap(string1, string2):
    length = min(len(string1), len(string2))
    length_i = length
    while (length_i > length//2):   
        if string1[-length_i:] == string2[:length_i]:
            return string1 + string2[length_i:]
        length_i-=1
    return ""

long('rosalind_long.txt')
    