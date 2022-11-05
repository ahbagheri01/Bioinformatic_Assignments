DNAs = []
f = open("rosalind_edta.txt","r")
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
S1 = DNAs[1]
S2 = DNAs[2]
f = open("A2.txt","w")
def d(s, t):
    n, m = len(s), len(t)
    assert (m != 0) and (n != 0), "one or more string is NULL"
    DPtable =  [[0 for j in range(n+1)] for _ in range(m+1)] # m * n
    for i in range(max(m,n)+1):
        DPtable[0][min(i,n)] = min(i,n)
        DPtable[min(i,m)][0] = min(i,m)
    for i in range(1, n+1):
        for j in range(1, m+1):
            right = DPtable[j][i-1] + 1
            down = DPtable[j-1][i] + 1
            diag = DPtable[j-1][i-1]
            if s[i-1] != t[j-1]:
                diag += 1
            DPtable[j][i] = min(right, down, diag)
    return DPtable
def printalign(s,t,DP):
    n, m = len(s), len(t)
    assert (m != 0) and (n != 0), "one or more string is NULL"
    sprime = ""
    tprime = ""

    while (n > 0 or m > 0):




DP = d(S1,S2)
f.write(str(DP[-1][-1]))
printalign(S1,S2,DP)
