import sys

filename = sys.argv[1]

complements = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C'
}

with open(filename) as f:
    dna = f.readline().strip()
    reverse_complement = ''.join([complements[nt] for nt in reversed(dna)])

    print(reverse_complement)
