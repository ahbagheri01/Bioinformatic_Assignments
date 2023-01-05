import numpy as np
f = open("rosalind_ba7e.txt","r")
bign = int(f.readline())
matrix = np.array([list(map(int, f.readline().split())) for _ in range(bign)])
new_node_counter = bign
def dprime(D,n):
    Ds = np.sum(D, axis=0)
    Dp = np.zeros(shape=(n, n))
    for i in range(n):
        for j in range(n):
            if i != j:
                Dp[i, j] = (n - 2) * D[i, j] - Ds[i] - Ds[j]
    return Dp,Ds
def new_d(D,n,i,j): # this function is coppied from internet for adding a col and row to D
    D = np.vstack([D, np.zeros(len(D))])
    D = np.hstack([D, np.zeros((len(D), 1))])
    for k in range(n):
        D[-1, k] = (D[i, k] + D[j, k] - D[i, j]) / 2
        D[k, -1] = D[-1, k]
    D = np.delete(D, i, axis=0)
    D = np.delete(D, i, axis=1)
    D = np.delete(D, j-1 , axis=0)
    D = np.delete(D, j-1 , axis=1)
    return D

def njoin(D,n,Nodes):
    if n == 2:
        return {Nodes[0]:{Nodes[1]:D[0,1]},Nodes[1]:{Nodes[0]:D[1,0]}}
    DP,Ds = dprime(D,n)
    i, j = np.argwhere(DP == np.min(DP))[0]
    delta = (Ds[i] - Ds[j]) / (n - 2)
    limb_i = (D[i, j] + delta) / 2
    limb_j = (D[i, j] - delta) / 2
    D = new_d(D,n,i,j)
    global new_node_counter
    m = new_node_counter
    new_node_counter += 1
    new_list = [i for i in Nodes]
    new_list.remove(Nodes[i])
    new_list.remove(Nodes[j])
    new_list.append(m)
    T = njoin(D, n - 1,new_list)
    nc = list(T[m].items())
    i,j = Nodes[i],Nodes[j]
    T[i] = {m:limb_i}
    T[j] = {m:limb_j}
    T[m] = {i:limb_i,j:limb_j}
    for k,v in nc:
        T[m][k] = v
        T[k][m] = v
    return T
T = njoin(matrix,bign,[i for i in range(bign)])
graph = []
class Node:
    def __init__(self,u,v,w):
        self.u = u
        self.v = v
        self.w = w
    def __str__(self) -> str:
        return f'{self.u}->{self.v}:{self.w:.3f}'
    def __lt__(self, other):
        # p1 < p2 calls p1.__lt__(p2)
        return (self.u < other.u) or (self.u == other.u and self.v < other.v)
    
    def __eq__(self, other):
        # p1 == p2 calls p1.__eq__(p2)
        return self.distance == other.distance
        
for k in T:
    for i in T[k]:
        graph.append(Node(k,i,T[k][i]))
graph = sorted(graph)
f = open("A17.txt","w")
f.write("\n".join([str(g) for g in graph]))