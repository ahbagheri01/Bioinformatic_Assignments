best_name = ""
best_score = 0.0
name = ""
score = 0.0
count = 1.0
f = open("rosalind_gc.txt","r")
for line in f:
    line = line.strip()
    if line[0] != ">":
        count += len(line)
        for c in line:
            if c == "C" or c == "G":
                score += 1
        continue
    if best_score < (score/count):
        best_score = (score/count)
        best_name = name
    score = 0
    count = 0
    name = line[1:]
f.close()
if best_score < (score/count):
    best_score = (score/count)
    best_name = name
print(best_name)
print(best_score * 100)

