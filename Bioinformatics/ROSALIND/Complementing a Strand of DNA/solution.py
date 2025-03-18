"""
    Solution by Zhean Ganituen (zrygan)
    For Complementing a Strand of DNA
"""

class Solution:
    @staticmethod
    def complement_dna(dna: str) -> str:
        # Complement of DNA is given by:
        #   A -> T (vice versa)
        #   C -> G
        if any(char not in ['A', 'T', 'C', 'G'] for char in dna):
            return None
        
        complement = ""

        # complement DNA
        for char in dna:
            match char:
                case "A":
                    complement += "T"
                case "T":
                    complement += "A"
                case "C":
                    complement += "G"
                case "G":
                    complement += "C"

        # reverse complement
        length = len(complement)
        complement = list(complement)
        for i in range(0, length // 2):
            j = length - i - 1
            complement[i], complement[j] = complement[j], complement[i]

        return "".join(complement)
        
dna = ""

with open("dataset.txt", "r") as f:
    dna = f.readline()

print(Solution.complement_dna(dna))