import numpy as np
dnaL = [len(i) for i in list(set(open("rosalind_asmq.txt","r").read().strip().split('\n')))]
dnaL.sort()
dnaL.reverse()
dnaLSUM = np.array(dnaL).cumsum()
open("A22.txt","w").write(f"{dnaL[np.argwhere(dnaLSUM > sum(dnaL) * 0.50)[0][0]]} {dnaL[np.argwhere(dnaLSUM > sum(dnaL) * 0.75)[0][0]]}")