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
    a,b,w = int(l[0]),int(d1[0]),int(d1[1])
    if a not in Nodes:
        Nodes[a] = Node(a)
    if b not in Nodes:
        Nodes[b] = Node(b)
    Nodes[a].add_e(b,w)
    Nodes[b].add_e(a,w)
print
matrix = [[0 for i in range(N)] for _ in range(N)]
def bfs(node):
    global matrix
    dis = dict()
    q = queue.Queue()
    dis[node] = 0
    q.put(node)
    while not q.empty():
        cur = q.get()
        print(cur)
        curnodeE = Nodes[cur].e
        curnodeW = Nodes[cur].w
        print(list(zip(curnodeE,curnodeW)))
        for u,w in zip(curnodeE,curnodeW):
            print(cur,u,w)
            if not u in dis:
                dis[u] = dis[cur] + w
                if u < N:
                    matrix[node][u] = dis[u]
                    matrix[u][node] = dis[u]
                q.put(u)
for i in range(N-1):
    print("s=",i)
    bfs(i)
print("\n".join([" ".join([str(n) for n in m]) for m in matrix]))
