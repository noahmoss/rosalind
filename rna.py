import sys

filename = sys.argv[1]

with open(filename) as f:
    dna = f.readline()
    rna = dna.replace('T', 'U').rstrip()
    print(rna)
