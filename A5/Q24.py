f = open("rosalind_ba9l.txt","r")
def create_indexor(dna,indexor):
    for i in range(len(dna)):
        for key in indexor:
            indexor[key][i+1] = indexor[key][i]
        indexor[dna[i]][i+1] = indexor[dna[i]][i] + 1
    return indexor
dna = str(f.readline().strip())
dnasort = list(dna)
dnasort.sort()
dnasort = "".join(dnasort)
queries = f.readline().strip().split()
indexor = {key:[0 for i in range(len(dna) + 1)] for key in ["A","C","G","T","$"]}
indexor = create_indexor(dna,indexor)
"""
BWMATCHING(FirstColumn, LastColumn, Pattern, LastToFirst)
    top ← 0
    bottom ← |LastColumn| − 1
    while top ≤ bottom
        if Pattern is nonempty
            symbol ← last letter in Pattern
            remove last letter from Pattern
            if positions from top to bottom in LastColumn contain an occurrence of symbol
                topIndex ← first position of symbol among positions from top to bottom in LastColumn
                bottomIndex ← last position of symbol among positions from top to bottom in LastColumn
                top ← LastToFirst(topIndex)
                bottom ← LastToFirst(bottomIndex)
            else
                return 0
        else
            return bottom − top + 1
"""
def BWmatch(dnasort, dna, q, indexor):
    top = 0 
    bottom = len(dna) - 1
    while top <= bottom:
        if len(q) > 0:
            c = q[-1]
            q = q[0:len(q)-1]
            if c in dna[top:bottom+1]:
                topindex = indexor[c][top]
                bottomindex = indexor[c][bottom+1] -1
                top = dnasort.index(c) + topindex
                bottom = dnasort.index(c) + bottomindex
            else:
                return 0
        else:
            break
    return bottom - top + 1
ans = []
for q in queries:
    ans.append(str(BWmatch(dnasort,dna,q,indexor)))
open("A24.txt","w").write(" ".join(ans))
can1 = " ".join(ans)
#print(" ".join(can1))
