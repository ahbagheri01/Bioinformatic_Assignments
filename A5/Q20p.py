#!/usr/bin/python

'''
Rosalind: Bioinformatics Stronghold
Problem: Genome Assembly Using Reads
URL: http://rosalind.info/problems/gasm/
Given: A collection S of (error-free) reads of equal length (not exceeding 
50 bp). In this dataset, for some positive integer k, the de Bruijn graph 
BkBk on Sk+1∪Srck+1 consists of exactly two directed cycles.
Return: A cyclic superstring of minimal length containing every read or its 
reverse complement.
'''
from itertools import chain

def cyclic_superstring(dna):
    print(dna)
    flatten = lambda listOfLists: chain.from_iterable(listOfLists)
    
    n = len(dna)
    l = len(dna[0])  # assumes all strings are the same length
    
    for k in range(l-1, 1, -1):
        adj = dict(flatten([[(d[i:i+k], d[i+1:i+k+1]) for i in range(l-k)] for d in dna]))
        first = kmer = next(iter(adj))
        superstring = ''
        
        while True:
            if kmer in adj:
                superstring += kmer[-1]
                kmer = adj.pop(kmer)
                if kmer == first:
                    print(k)
                    print(first)
                    print(adj)
                    print(superstring)
                    return superstring
            else:
                break

def reverse_comp(dnaStrand):
	complementDNA = ""


	dnaSequence = list(dnaStrand)
	dnaSequence.reverse()

	dnaStrand = ''.join(dnaSequence)
	complementDict = {"C": "G", "G": "C", "T": "A", "A": "T"}

	for base in dnaStrand:
		complementDNA += complementDict[base]

	return complementDNA

def main():
    with open('rosalind_gasm.txt', 'r') as infile:
        dna = infile.read().strip().split('\n')
        dna = list(set(dna + [reverse_comp(i) for i in dna])) # Add the reverse complement of each string.
    
    with open('A20.txt', 'w') as outfile:
        print(cyclic_superstring(dna))
        outfile.write(cyclic_superstring(dna))
    

if __name__ == '__main__':
    main()