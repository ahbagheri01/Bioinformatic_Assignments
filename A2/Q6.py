import numpy as np
import itertools
DNAs = []
f = open("rosalind_mult.txt","r")
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
f = open("A6.txt","w") 
permutations =  list(itertools.product([0,1], repeat=len(DNAs)))
permutations.remove((0,0,0,0))
#f = open("test1.txt","w")
def d(DNAs):
    l1,l2,l3,l4 = len(DNAs[0]), len(DNAs[1]), len(DNAs[2]), len(DNAs[3])
    indel = lambda index,pos,permutation : "-" if not permutation[index] else  DNAs[index][pos - 1]
    previous = lambda pos,permutation : tuple([pos[i] - permutation[i] for i in range(len(pos))])
    check_condition = lambda index,permutation: sum([not permutation[i] or index[i] > 0 for i in range(len(index))]) 
    DP =  np.zeros((l1+1,l2+1,l3+1,l4+1))
    keep_trace = np.array(DP,dtype = object)
    keep_trace[:,:,:,:] = None
    for i in range(1,max(l1,l2,l3,l4)+1):
        DP[min(i,l1),0,0,0] = min(i,l1) * -3
        keep_trace[min(i,l1),0,0,0] = [1, 0, 0, 0]
        DP[0,min(i,l2),0,0] = min(i,l2) * -3
        keep_trace[0,min(i,l2),0,0] = [0,1, 0, 0]
        DP[0,0,min(i,l3),0] = min(i,l3) * -3
        keep_trace[0,0,min(i,l3),0] = [0, 0, 1, 0]
        DP[0,0,0,min(i,l4)] = min(i,l4) * -3
        keep_trace[0,0,0,min(i,l4)] = [0, 0, 0, 1]
    for i in range(l1+1):
        for j in range(l2+1):
            for k in range(l3+1):
                for h in range(l4+1):
                    if sum([i,j,k,h]) <= 1:
                        continue
                    best_score = -np.inf
                    best_permutation = None
                    for permutation in permutations:
                        if check_condition([i,j,k,h], permutation) == 4:
                            s = np.array([indel(0,i,permutation),indel(1,j,permutation),indel(2,k,permutation),indel(3,h,permutation)])
                            score = DP[previous([i,j,k,h],permutation)]
                            score += -6 + sum([sum([s[n] == s[m] for m in range(n+1,4)]) for n in range(4)])
                            if score > best_score:
                                best_score,best_permutation = score,permutation
                    DP[i, j, k, h] = best_score
                    keep_trace[i, j, k, h] = best_permutation
    return DP,keep_trace

def align(DNAs, dp, trace):
    l1,l2,l3,l4 = len(DNAs[0]), len(DNAs[1]), len(DNAs[2]), len(DNAs[3])
    final_align = ["" for _ in range(len(DNAs))]
    indel = lambda index,pos,permutation,final_align : ("-" if not permutation[index] else  DNAs[index][pos - 1]) + final_align[index][:]
    while sum([l1,l2,l3,l4]) >= 1:
        permutation = trace[l1,l2,l3,l4]
        perm = [l1,l2,l3,l4]
        for i in range(len(perm)):
            final_align[i] = indel(i,perm[i],permutation,final_align)
        l1,l2,l3,l4 = l1 - permutation[0], l2 - permutation[1], l3 - permutation[2], l4 - permutation[3]
    return final_align
dp, keep_trace = d(DNAs)
f.write(f"{int(dp[-1,-1,-1,-1])}\n")
aligns = align(DNAs,dp,keep_trace)
f.write("\n".join(aligns))


                        
                    

                        


                        