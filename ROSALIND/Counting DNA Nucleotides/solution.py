"""
    Solution by Zhean Ganituen (zrygan)
    For ROSALIND Counting DNA Nucleotides
"""

import fileinput

count_a = 0 
count_c = 0 
count_g = 0 
count_t = 0 
dna = ''

with open('dataset.txt', 'r') as f:
    dna = f.read()

for char in dna:
    if char == "A":
        count_a += 1
    elif char == "C":
        count_c += 1
    elif char == "G":
        count_g += 1
    elif char == "T":
        count_t += 1

print(count_a, count_c, count_g, count_t)
