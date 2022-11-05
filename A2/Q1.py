DNAs = []
f = open("rosalind_pdst.txt","r")
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
def d(si,sj):
    n = len(si)
    d = 0
    for i in range(n):
        if si[i] != sj[i]:
            d += 1
    return d/n
N = len(DNAs)
matrix = [[0.0 for i in range(N)] for i in range(N)]
for i in range(N):
    for j in range(i):
        matrix[i][j] = matrix[j][i] = d(DNAs[i],DNAs[j])
res = "\n".join([" ".join([str(k) for k in matrix[i]]) for i in range(N)])
f = open("A1.txt","w")
f.write(res)
f.close()



