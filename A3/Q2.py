def complement(dna):
    dna = dna[::-1]
    dna = dna.replace("A","O")
    dna = dna.replace("C","F")
    dna = dna.replace("T","A")
    dna = dna.replace("G","C")
    dna = dna.replace("O","T")
    dna = dna.replace("F","G")
    return dna
def matdist(dna1,dna2):
    s = 0
    for i in range(len(dna1)):
        s += 1 if dna1[i]!= dna2[i] else 0
        if s >= 2:
            return s
    return s
DNAs = []
f = open("rosalind_corr.txt","r")
sample = ""
for line in f:
    line = line.strip()
    if line[0] != ">":
        sample += line
    else:
        DNAs.append(sample)
        sample = ""
f.close()
DNAs.append(sample)
DNAs = DNAs[1:]
f = open("A2.txt","w")
correct = []
problem = []
for dna in DNAs:
    if DNAs.count(dna) > 1 or complement(dna) in DNAs:
        correct.append(dna)
    else:
        problem.append(dna)
final = []
for dna in problem:
    for cdna in correct:
        # print(dna)
        # print(cdna)
        if matdist(dna,cdna) == 1:
            final.append(f"{dna}->{cdna}")
            break
        elif  matdist(dna,complement(cdna)) == 1:
            final.append(f"{dna}->{complement(cdna)}")
            break
f.write("\n".join(final).strip())
f.close()



