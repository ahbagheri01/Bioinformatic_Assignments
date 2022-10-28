import itertools
with open("rosalind_lexf.txt","r") as f:
    lines = f.readlines()
alphabet = lines[0].strip().split(" ")
n = int(lines[1])
base = len(alphabet)
f = open("A3.txt","w")
def numberToBase(n, b , l):
    if n == 0:
        return [0]
    digits = [0] * l
    count = 0
    while n:
        digits[l - count- 1] = int(n%b)
        count += 1
        n //= b
    return digits
f.write(f"{alphabet[0]}"*n+"\n")
for i in range(1,base ** n):
    f.write(''.join([alphabet[index] for index in numberToBase(i, base, n)]))
    f.write("\n")
# for x in itertools.product(alphabet, repeat=n):
#     f.write(''.join(x))
#     f.write("\n")
