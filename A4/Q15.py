import numpy as np
f = open("rosalind_ba7c.txt","r")
bign = int(f.readline())
new_node_counter = bign
matrix = np.array([list(map(int, f.readline().split())) for _ in range(bign)])
f = open("A15.txt","w")

def findlimb(D, node):
    N = len(D)
    pairs = [(i,j) for i in range(N) for j in range(N)]
    return min([matrix[i][node] + matrix[j][node] - matrix[i][j] for (i,j) in pairs if i != node and j != node])//2

def findtriple(D, n):
    target = n-1
    for i in range(n):
        for k in range(n):
            if D[i, k] == D[i, target] + D[target, k]:
                return i, target, k
    return None

def start_dfs(i,k,T):
    visited = {i:False for i in T}
    path =  dfs(i,k,T,visited,[])
    print(T,path)
    return path
def dfs(i,k,T,visited,path=[]):
    if i == k:
        path.append(i)
        return path
    if visited[i]:
        return None
    print(i,path,visited)
    v = [node for node in T[i]]
    visited[i] = True
    path.append(i)
    for node in v :
        p = dfs(node,k,T,visited,path)
        if p != None:
            return p
    path.remove(i)
    return None
        
        
    

def find_addtree(D,n):
    if n == 1:
        return {0:{1:D[0,1]},1:{0:D[1,0]}}
    limb = findlimb(D,n)
    for k in range(n):
        D[k, n] -= limb
        D[n, k] = D[k, n]
    i, n, k = findtriple(D, len(D))
    x = D[i, n]
    D = np.delete(D, n, axis=0)
    D = np.delete(D, n, axis=1)
    T = find_addtree(D, n - 1)
    path = start_dfs(i,k,T)

    i,j,d,dprime = 0,0,0,0
    for v in range(len(path)-1):
        i,j = path[v],path[v+1]
        dprime = d
        d += T[i][j]
        if d > x:
            break
    v,u = i,j
    newnode = v
    if dprime != x:
        T[v].pop(u)
        T[u].pop(v)
        global new_node_counter
        newnode = new_node_counter
        new_node_counter += 1
        T[v][newnode] = x - dprime
        T[u][newnode] = d - x 
        T[newnode] = {}
        T[newnode][v] = x - dprime
        T[newnode][u] = d - x 
    T[n] = {}
    T[n][newnode] = limb
    T[newnode][n] = limb
    return T

T = find_addtree(matrix,bign-1)    
T = {key : {k : T[key][k] for k in sorted(T[key])} for key in sorted(T)}
for key in T:
    for k in T[key]:
        f.write(f"{key}->{k}:{T[key][k]}\n")