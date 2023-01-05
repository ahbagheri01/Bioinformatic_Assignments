import sys
def flatten(l):
    return [i for k in l for i in k]
N = 0
length = 0
complementDict = {"C": "G", "G": "C", "T": "A", "A": "T"}
def find_k_meres_nodes(DNAs,k):
    return [[[dna[i:i+k], dna[i+1:i+k+1]] for i in range(length-k)] for dna in DNAs]

def create_graph(k_meres):
    return {item[0] : item[1] for item in flatten(k_meres)}

def superstring(dna,k):
    k_meres = find_k_meres_nodes(dna,k)
    graph = create_graph(k_meres)
    return graph

def reverse_comp(dnaStrand):
    return "".join([complementDict[base] for base in  list(dnaStrand)[::-1]])

f = open("rosalind_gasm.txt","r")
dna = f.read().strip().split('\n')
dna = list(set(dna + [reverse_comp(i) for i in dna]))
N,length = len(dna),len(dna[0])
for k in range(length-1,1,-1):
    graph = superstring(dna,k)
    firstnode = [key for key in graph][0]
    nextnode = firstnode
    final = ''
    while True:
        if nextnode in graph:
            final += nextnode[-1]
            nextnode = graph.pop(nextnode)
            if nextnode == firstnode:
                open("A20.txt","w").write(final)
                sys.exit()
        else:
            break