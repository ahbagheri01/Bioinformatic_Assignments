
f = open("rosalind_revc.txt","r")
DNA = f.readlines()
DNA = "".join([dna.strip() for dna in DNA])
#print(DNA)
f.close()
DNA = DNA[::-1]
#print(DNA)
DNA = DNA.replace("A","O")
DNA = DNA.replace("C","F")
DNA = DNA.replace("T","A")
DNA = DNA.replace("G","C")
DNA = DNA.replace("O","T")
DNA = DNA.replace("F","G")
f = open("A2.txt","w")
f.write(DNA)
f.close()


