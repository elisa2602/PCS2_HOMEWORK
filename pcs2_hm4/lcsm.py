from Bio import SeqIO


sequences = []
handle  = open('rosalind_lcsm (1).txt','r')
for seq_record in SeqIO.parse(handle,'fasta'):
    seq = ''
    for nucleotide in seq_record.seq:
        seq += nucleotide
    sequences.append(seq)

srt_seq = sorted(sequences, key=len)  #sort a DNA seq by length    
short_seq = srt_seq[0]                   
comp_seq = srt_seq[1:]                   
motif = ''    

for i in range(len(short_seq)):          
    for j in range(i, len(short_seq)):   
        m = short_seq[i:j + 1]           
        found = False                   
        for sequ in comp_seq:            
            if m in sequ:                
                found = True            
            else:                        
                found = False           
                break                   
        if found and len(m) > len(motif):
            motif = m                    
print(motif)
