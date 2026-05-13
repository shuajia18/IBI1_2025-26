import os
import pandas as pd

#change working directory to where download file exists
os.chdir('C:/Users/shuaj/Desktop/IBI/practical 3/IBI1_2025-26/Practical13')

#read the content of files 
def readfile(files):
    sequence = ''
    with open(files,'r') as f:
        for line in f:
            if not line.startswith('>'):
                sequence = sequence+ line.strip()
    return sequence
human_seq =readfile('DLX5_human_P56178.fasta')
mouse_seq =readfile('DLX5_mouse_P70396.fasta')
random_seq=readfile('random_protein_seq.fasta')

#read matrix
matrix = pd.read_csv('BLOSUM62_matrix', sep='\s+', index_col=0)

def sim(seq1,seq2,name):
    similarity=0
    for i in range(len(seq1)):
        if seq1[i] == seq2[i]:
            similarity = similarity +1
    print(f'The number of the same amino acids between {name} is {similarity}')
    #get the percentage
    percentage=(similarity*100)/len(seq1)
    print(f'The percentage identity between {name} is {percentage}%')

    #get the score
    total=0
    self_t=0
    for i in range(len(seq1)):
        aa_1=seq1[i]
        aa_2=seq2[i]
        current_score=matrix.loc[aa_1,aa_2]
        current_self=matrix.loc[aa_1,aa_1]
        total= total+current_score
        self_t=self_t+current_self
    print(f'The alignment score of {name} is {total}')
    
    #normalized   
    normalized=total/self_t
    print(f'The normalized alignment score of {name} is {normalized}')

a=sim(human_seq,mouse_seq,'human and mouse')
b=sim(human_seq,random_seq,'human and random seq')
c=sim(mouse_seq,random_seq,'mouse and random seq')











