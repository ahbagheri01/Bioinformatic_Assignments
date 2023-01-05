import numpy as np
dna = str(open("rosalind_ba9j.txt","r").readline().strip())
N = len(dna)
s = ["" for _ in range(N)]
index = 0
for j in range(N):
    for i in range(N):
        s[i] = dna[i] + s[i]
    s.sort()
for i in range(N):
    if s[i][-1] == "$":
        index = i
        break
print(s[index])
open("A23.txt","w").write(s[index])



