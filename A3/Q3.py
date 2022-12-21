def complement(dna):
    dna = dna[::-1]
    dna = dna.replace("A","O")
    dna = dna.replace("C","F")
    dna = dna.replace("T","A")
    dna = dna.replace("G","C")
    dna = dna.replace("O","T")
    dna = dna.replace("F","G")
    return dna
DNAs = {i.strip() for i in open("rosalind_dbru.txt","r").readlines()}
DNAsr = {complement(i) for i in DNAs}
DNA = {*DNAs,*DNAsr}
print(DNA)

