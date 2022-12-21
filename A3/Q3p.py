inputFilePath = "rosalind_dbru.txt"
outputFilePath=open("output.txt", "w")

class Node:
	"""This node is the main object used for the debrujin graph"""
	def __init__(self,kmer):
	   self.kmer = kmer
	   self.edges = set()
	def __str__(self):
		return "kmer = {}\n edges = {}".format(self.kmer,self.edges)


def reverse_comp(dnaStrand):
	"""This function gets the reverse complement of the strand"""
	complementDNA = ""

	dnaSequence = list(dnaStrand)
	dnaSequence.reverse()

	dnaStrand = ''.join(dnaSequence)
	complementDict = {"C": "G", "G": "C", "T": "A", "A": "T"}

	for base in dnaStrand:
		complementDNA += complementDict[base]

	return complementDNA

def kmers_list(m, string):
	"""This function produces the kmer list"""
	Kmers = []
	for i in range(len(string) - m + 1):
		Kmers.append(string[i: i + m])
	return Kmers


if __name__ == "__main__":
	dna_list = []
	with open(inputFilePath) as f:
		dna_list = f.read().splitlines()

	dna_list+=[reverse_comp(x) for x in dna_list]

	kmerLength = len(dna_list[0]) - 1

	node_dict = {}
	for dna in dna_list:
		last_node = None
		for kmer in kmers_list(kmerLength, dna):
				if kmer not in node_dict:
					node_dict[kmer] = Node(kmer)
				if last_node:
					last_node.edges.add(node_dict[kmer])
				last_node = node_dict[kmer]



	for kmer, node in sorted(node_dict.items()):
		for edge in node.edges:
			outputFilePath.write( "({0}, {1})".format(kmer,edge.kmer) + "\n")