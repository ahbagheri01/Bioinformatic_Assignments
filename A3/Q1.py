import json
from collections import defaultdict
freq = defaultdict(lambda : 0)
table = json.load(open("rnacondont.json","r"))
for k,v in table.items():
    freq[v] += 1
dna = open("rosalind_mrna.txt","r").read().strip()
n = freq["Stop"]
for s in dna:
    n  = (n*freq[s])%1000000
open("A1.txt","w").write(str(int(n)))