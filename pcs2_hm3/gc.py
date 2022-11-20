from Bio import SeqIO                      
GC = 0                                     
handle = open('rosalind_gc (2).txt', 'r')     
for record in SeqIO.parse(handle, 'fasta'):
    count = 0                              
    t_count = 0                         
    for i in record.seq:                  
        t_count = t_count + 1        
        if i == 'G' or i == 'C':         
            count = count + 1              
    percent = count/t_count*100         
    if percent > GC:                       
        GC = percent                       
        ID = record.id                     
print(ID)                                  
print(GC)                                  
handle.close()   
