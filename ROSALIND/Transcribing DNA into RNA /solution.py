"""
    Solution by Zhean Ganituen (zrygan)
    For ROSALIND Transcribing DNA into RNA
"""

class Solution:
    @staticmethod
    def dna_to_rna(dna: str) -> str:    
        if any(char not in ['A', 'C', 'G', 'T'] for char in dna):
            return None
        
        rna = list(dna)

        for i, char in enumerate(dna):
            if char == "T":
                rna[i] = "U"

        return "".join(rna)

dna = None

with open('dataset.txt', 'r') as f:
    dna = f.readline()

print(Solution.dna_to_rna(dna)) 
