from collections import defaultdict
import queue
f = open("rosalind_ba7a.txt","r")
N = int(f.readline())
class Node:
    def __init__(self,n):
        self.num = n
        self.e = []
        self.w = []
    def add_e(self,e1,w):
        self.e.append(e1)
        self.w.append(w)
Nodes = defaultdict(lambda n : Node(n))
for line in f.readlines():
    l = line.strip()
    d = l.split('->')
    d1 = d[1].split(':')
    a,b,w = int(d[0]),int(d1[0]),int(d1[1])
    if not a in Nodes:
        Nodes[a] = Node(a)
    Nodes[a].add_e(b,w)

matrix = [[0 for i in range(N)] for _ in range(N)]
def bfs(node):
    global matrix
    dis = dict()
    q = queue.Queue()
    dis[node] = 0
    q.put(node)
    while not q.empty():
        cur = q.get()
        curnodeE = Nodes[cur].e
        curnodeW = Nodes[cur].w
        for u,w in zip(curnodeE,curnodeW):
            if not u in dis:
                dis[u] = dis[cur] + w
                if u < N:
                    matrix[node][u] = dis[u]
                    matrix[u][node] = dis[u]
                q.put(u)
for i in range(N-1):
    bfs(i)

for i in range(N):
    for j in range(N):
        if (matrix[i][j] != matrix[j][i]):
            print("error")
f = open("A13.txt","w")
f.write("\n".join([" ".join([str(n) for n in m]) for m in matrix]))
f.close()