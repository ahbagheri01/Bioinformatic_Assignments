f = open("rosalind_ba7b.txt","r")
n = int(f.readline())
node = int(f.readline())
matrix = [list(map(int, f.readline().split())) for _ in range(n)]
f = open("A14.txt","w")
pairs = [(i,j) for i in range(n) for j in range(n)]
f.write(str(min([matrix[i][node] + matrix[j][node] - matrix[i][j] for (i,j) in pairs if i != node and j != node])//2))
