import numpy as np
f = open("rosalind_ba7d.txt","r")
bign = int(f.readline())
matrix = np.array([list(map(int, f.readline().split())) for _ in range(bign)])
class cluster:
    def __init__(self,nodes,i,age):
        self.nodes = nodes
        self.n = i
        self.age = age
    def __eq__(self, __o: object) -> bool:
        return __o.n == self.n
    def __hash__(self) -> int:
        return hash(self.n)
    def __str__(self) -> str:
        return f"{self.n}->{self.age}"

def cluster_d(c_i, c_j):
    global matrix
    distance = 0
    for i in c_i.nodes:
        for j in c_j.nodes:
            distance += matrix[i,j]
    distance /= len(c_i.nodes) * len(c_j.nodes)
    return distance
def merge(c_i, c_j,n):
    return cluster(c_i.nodes + c_j.nodes, n , cluster_d(c_i, c_j)/2)

def closeest_pair(clusters):
    v,u = 0,0
    d = float("inf")
    for i in range(len(clusters)):
        for j in range(i+1,len(clusters)):
            dis = cluster_d(clusters[i],clusters[j])
            if dis < d:
                d = dis
                v,u = i,j
    return v,u

def upgma(D, n):
    clusters = [cluster([i],i,0) for i in range(n)]
    T = {c:[] for c in clusters}
    while len(clusters) > 1:
        # find closest clusters
        i,j = closeest_pair(clusters)
        ci,cj = clusters[i], clusters[j]
        # merge clusters
        c_new = merge(ci, cj , len(T))
        T[c_new] = []
        T[c_new].append(ci)
        T[c_new].append(cj)
        T[ci].append(c_new)
        T[cj].append(c_new)
        # remove clusters
        clusters.remove(ci)
        clusters.remove(cj)
        clusters.append(c_new)
    c = clusters[0]
    return T[c],T
root , T = upgma(matrix,bign)
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
        graph.append(Node(k.n,i.n,abs(k.age - i.age)))
graph = sorted(graph)
f = open("A16.txt","w")
f.write("\n".join([str(g) for g in graph]))



