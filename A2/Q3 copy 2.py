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
# def p(DP):
#     return "\n".join([" ".join([str(k) for k in DP[i]]) for i in range(len(DP))])
def printalign(v,w,S, backtrack):
    i,j = len(v), len(w)
    v_aligned, w_aligned = v, w

    # Get the maximum score, and the corresponding backtrack starting position.
    matrix_scores = [S[0][i][j], S[1][i][j], S[2][i][j]]
    max_score = max(matrix_scores)
    backtrack_matrix = matrix_scores.index(max_score)

    # Quick lambda function to insert indels.
    insert_indel = lambda word, i: word[:i] + '-' + word[i:]

    # Backtrack to the edge of the matrix starting bottom right.
    while i*j != 0:
        print(backtrack_matrix,i,j)
        #print(backtrack_matrix)
        if backtrack_matrix == 0:  # Lower backtrack matrix conditions.
            if backtrack[0][i][j] == 1:
                backtrack_matrix = 1
            i -= 1
            w_aligned = insert_indel(w_aligned, j)

        elif backtrack_matrix == 1:  # Middle backtrack matrix conditions.
            if backtrack[1][i][j] == 0:
                backtrack_matrix = 0
            elif backtrack[1][i][j] == 2:
                backtrack_matrix = 2
            else:
                i -= 1
                j -= 1

        else:  # Upper backtrack matrix conditions.
            if backtrack[2][i][j] == 1:
                backtrack_matrix = 1
            j -= 1
            v_aligned = insert_indel(v_aligned, i)

    # Prepend the necessary preceeding indels to get to (0,0).
    for _ in range(i):
        w_aligned = insert_indel(w_aligned, 0)
    for _ in range(j):
        v_aligned = insert_indel(v_aligned, 0)
    print(v_aligned)
    print(w_aligned)
    return v_aligned, w_aligned








DP,trace = d(S1,S2)
f.write(f"{str(max([DP[0][-1][-1], DP[1][-1][-1], DP[2][-1][-1]]))}\n")
s,t = printalign(S1,S2,DP,trace)
f.write(f"{s}\n{t}")
