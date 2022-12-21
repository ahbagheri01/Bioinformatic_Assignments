DNAs = []
f = open("rosalind_dbru.txt","r")
sample = ""
def reverse_comp(dnaStrand):
	complementDNA = ""

	dnaSequence = list(dnaStrand)
	dnaSequence.reverse()

	dnaStrand = ''.join(dnaSequence)
	complementDict = {"C": "G", "G": "C", "T": "A", "A": "T"}

	for base in dnaStrand:
		complementDNA += complementDict[base]

	return complementDNA
DNAs = f.readlines()
f.close()
f = open("A19.txt","w")
ALLDNA = set()
for item in DNAs:
    dna = item.strip()
    ALLDNA.add(reverse_comp(dna))
    ALLDNA.add(dna)
adj = set()
N = len(dna)
for dna in ALLDNA:
    adj.add(f"({dna[0:N-1]}, {dna[1:N]})")
f.write("\n".join(list(adj)))
f.close()


