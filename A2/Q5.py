import blosum as bl
matrix = bl.BLOSUM(62)
DNAs = []
f = open("rosalind_laff.txt","r")
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
f = open("A5.txt","w")

def d(s, t, epsilon = 1,sigma = 11):
    n, m = len(s), len(t)
    assert (m != 0) and (n != 0), "one or more string is NULL"
    DPS =  [[0 for j in range(m+1)] for _ in range(n+1)]
    DPU =  [[0 for j in range(m+1)] for _ in range(n+1)]
    DPM =  [[0 for j in range(m+1)] for _ in range(n+1)]
    keep_trace = [[0 for j in range(m+1)] for _ in range(n+1)] #3 * n * m 
    best_i,best_j, best_val = 0,0, -sigma * (max(n,m)**2)
    for i in range(1, n+1):
        for j in range(1, m+1):
            DPS[i][j] = max([DPS[i-1][j] - epsilon, DPM[i-1][j] - sigma])
            DPU[i][j] = max([DPU[i][j-1] - epsilon, DPM[i][j-1] - sigma])
            middle = [DPS[i][j], DPU[i][j],DPM[i-1][j-1] + matrix[s[i-1]+ t[j-1]],0]
            DPM[i][j] = max(middle)
            keep_trace[i][j] = middle.index(DPM[i][j])
            if DPM[i][j] > best_val :
                best_i, best_j, best_val = i,j,DPM[i][j]
    return DPM,keep_trace,best_i,best_j

            

def printalign(s,t,DP, trace,i,j):
    n, m = len(s), len(t)
    assert (m != 0) and (n != 0), "one or more string is NULL"
    sprime,tprime = s[:i],t[:j]
    while (DP[i][j] != 0 and i > 0 and j > 0 ):
        # print(f"{start_index}",n,m)
        if trace[i][j] == 0 : 
            i -= 1
        if trace[i][j] == 1 :
            j -= 1
        if trace[i][j] == 2 :
            i -= 1
            j -= 1
    sprime = sprime[i:]
    tprime = tprime[j:]   
    return sprime,tprime

DP,trace,i,j = d(S1,S2)
f.write(f"{str(int(DP[i][j]))}\n")
s,t = printalign(S1,S2,DP,trace,i,j)
f.write(f"{s}\n{t}")
