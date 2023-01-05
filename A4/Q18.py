input_file = open("rosalind_ba7f.txt", "r")
lines = input_file.readlines()
n = int(lines[0].rstrip())
lines = lines[1:]
len_leaf = 0
T = {}
root = 0

class Node:
    def __init__(self,index,leaf = False,dna = ""):
        self.index = index
        self.tag = 0
        self.dna = ['*' for _ in  range(len_leaf)] 
        self.backtrack = [{} for _ in  range(len_leaf)]
        self.c = []
        self.p = []
        self.leaf = leaf
        self.leaf_dna = dna
        if leaf:
            self.dna = dna
        self.s = [{} for _ in  range(len_leaf)] 
    def add_edgec(self,n):
        self.c.append(n)
    def add_edgep(self,p):
        self.p.append(p)
    
    def __repr__(self) -> str:
        return f"{self.index},{self.tag},{''.join(self.dna)},{self.s[4]}\
            {self.backtrack[4]}"

def add_to_T(n):
    global T
    if not (n in T):
        T[n] = Node(n)
maximum = 0
for line in lines:
    nodes = line.rstrip().split('->')
    if nodes[1].isdigit():
        if maximum < int(nodes[0]):
            maximum = int(nodes[0])
        if maximum < int(nodes[1]):
            maximum = int(nodes[1])
    else:
        len_leaf = len(nodes[1])
maximum += 1
alphabet = ['A', 'C', 'T', 'G']

def get_triped():
    l = []
    for key,val in T.items():
        if val.tag == 0 and sum([T[k].tag == 1 for k in val.c]) == len(val.c) and (not val.leaf):
            return val
    return None
    
def get_minimum_val(node,i,k):
    allc = 0
    l = {}
    for cn in node.c:        
        minv = float("inf")
        minc = ""
        for c in alphabet:
            if node.index == root and i == 4 and c == "A":
                print("h",T[cn].s[i],c,k)
            if minv > (T[cn].s[i][c] + (0  if c == k else 1)):
                minv = T[cn].s[i][c] + (0  if c == k else 1)
                minc = c
        l[cn] = minc
        allc += minv
    if node.index == root and i == 4:
        print(l,k,node)
    node.backtrack[i][k] = l
    return allc



    

def small_parsimony(i):
    for key,val in T.items():
        val.tag = 0
        if val.leaf:
            val.tag = 1
            for c in alphabet:
                if c == val.dna[i]:
                    val.s[i][c] = 0 
                else:
                    val.s[i][c] = float("inf")
    while True:
        tr = get_triped()
        if not tr:
            break
        tr.tag = 1
        for c in alphabet:
            tr.s[i][c]  = get_minimum_val(tr,i,c)
    minc = "-"
    minv = float("inf")
    for c in alphabet:
        if minv > T[root].s[i][c] :
            minv = T[root].s[i][c]
            minc = c
    T[root].dna[i] = minc

    return minv



for line in lines:
    nodes = line.rstrip().split('->')
    if nodes[1].isdigit():
        src, dest = int(nodes[0]), int(nodes[1])
        add_to_T(src)
        add_to_T(dest)
        T[src].add_edgec(dest)
        T[dest].add_edgep(src)
        root = src
    else:
        src, dest = int(nodes[0]), nodes[1]
        len_leaf = len(dest)
        add_to_T(src)
        destnode = Node(maximum,leaf=True, dna= dest)
        T[maximum] = destnode
        T[src].add_edgec(maximum)
        T[maximum].add_edgep(src)
        maximum += 1
score = 0
def backtrace(node,i):
    minc = T[node].dna[i]
    if node == root and i == 4:
        print(minc,T[root].backtrack[4])
    for n in T[node].c:
        if not T[n].leaf:
            T[n].dna[i] = T[node].backtrack[i][minc][n]
            backtrace(n,i)   
for i in range(len_leaf):
    score += small_parsimony(i)
    backtrace(root,i)
print("here")
f = open("A18.txt","w")
f.write(str(score))
f.write("\n")
haming = lambda x,y : sum([x[i] != y[i] for i in range(len_leaf)])

def back(T,node):
    for c in T[node].c:
        f.write("".join(T[node].dna)+"->"+"".join(T[c].dna)+":"+str(int(haming(T[node].dna,T[c].dna))))
        f.write("\n")
        f.write("".join(T[c].dna)+"->"+"".join(T[node].dna)+":"+str(int(haming(T[node].dna,T[c].dna))))
        f.write("\n")
        back(T,c)
back(T,root)



