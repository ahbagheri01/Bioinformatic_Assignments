#pip install blosum
import blosum as bl
matrix = bl.BLOSUM(62)
# print(matrix)
DNAs = []
f = open("rosalind_gaff.txt","r")
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
f = open("A3.txt","w")

def d(s, t, epsilon = 1,sigma = 11):
    n, m = len(s), len(t)
    assert (m != 0) and (n != 0), "one or more string is NULL"
    DPtable =  [[[0 for j in range(m+1)] for _ in range(n+1)] for d in range(3)] #3 * n * m 
    keep_trace = [[[0 for j in range(m+1)] for _ in range(n+1)] for d in range(3)] #3 * n * m 
    for i in range(1, n+1):
        DPtable[0][i][0] = -sigma - (i-1)*epsilon
        DPtable[1][i][0] = -sigma - (i-1)*epsilon
        DPtable[2][i][0] = -max(n,m)*sigma # moving only in right
    for i in range(1, m+1):
        DPtable[2][0][i] = -sigma - (i-1)*epsilon
        DPtable[1][0][i] = -sigma - (i-1)*epsilon
        DPtable[0][0][i] = -max(n,m)*sigma

    for i in range(1, n+1):
        for j in range(1, m+1):
            lower = [DPtable[0][i-1][j] - epsilon, DPtable[1][i-1][j] - sigma]
            DPtable[0][i][j] = max(lower)
            keep_trace[0][i][j] = lower.index(DPtable[0][i][j])

            upper = [DPtable[2][i][j-1] - epsilon, DPtable[1][i][j-1] - sigma]
            DPtable[2][i][j] = max(upper)
            keep_trace[2][i][j] = upper.index(DPtable[2][i][j])
            
            middle = [DPtable[0][i][j], DPtable[1][i-1][j-1] + matrix[s[i-1]+ t[j-1]], DPtable[2][i][j]]
            DPtable[1][i][j] = max(middle)
            keep_trace[1][i][j] = middle.index(DPtable[1][i][j])
            
           
            
    return DPtable,keep_trace
def printalign(s,t,DP, trace):
    n, m = len(s), len(t)
    assert (m != 0) and (n != 0), "one or more string is NULL"
    sprime,tprime = s,t
    start_index = [DP[0][n][m], DP[1][n][m], DP[2][n][m]].index(max([DP[0][n][m], DP[1][n][m], DP[2][n][m]]))
    while (n > 0 and m > 0):
        # print(f"{start_index}",n,m)
        if start_index == 0: # lower go up and down or to middle
            start_index = 1 if trace[0][n][m] == 1 else 0
            n -=1
            tprime = tprime[:m] + "-" + tprime[m:]

        elif start_index == 2:
            start_index = 1 if trace[2][n][m] == 1 else 2
            m -= 1
            sprime = sprime[:n] + "-" + sprime[n:]

        else:
            start_index = trace[1][n][m]
            if start_index == 1:
                n -= 1
                m -= 1
        # print(f"{sprime}\n{tprime}\n")  
    for _ in range(n):
        tprime = "-" + tprime
    for _ in range(m):
        sprime = "-" + sprime
    # print(f"{sprime}\n{tprime}\n")    
    return sprime,tprime








DP,trace = d(S1,S2)
f.write(f"{str(int(max([DP[0][-1][-1], DP[1][-1][-1], DP[2][-1][-1]])))}\n")
s,t = printalign(S1,S2,DP,trace)
f.write(f"{s}\n{t}")
