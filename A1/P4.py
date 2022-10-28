total_node = 0
class Node:
    def __init__(self,id) -> None:
        self.node = id
        self.edges = {}
    def parse(self,patern):
        if len(patern) == 0:
            return
        c = patern[0]
        nx = self.edges.get(c,None)
        if nx:
            nx.parse(patern= patern[1:])
        else:
            global total_node
            total_node += 1
            new_node = Node(total_node)
            self.edges[c] = new_node
            print(f"{self.node}->{new_node.node}:{c}")
            new_node.parse(patern= patern[1:])
with open("rosalind_ba9a.txt","r") as f:
    lines = f.readlines()
root = Node(total_node)
for line in lines:
    line = line.strip()
    root.parse(line)
