import itertools
with open("rosalind_lexf.txt","r") as f:
    lines = f.readlines()
alphabet = lines[0].strip().split(" ")
n = int(lines[1])
base = len(alphabet)
f = open("A3.txt","w")
for x in itertools.product(alphabet, repeat=n):
    f.write(''.join(x))
    f.write("\n")
