"""
    Solution by Zhean Ganituen (zrygan)
    For Leetcode #191
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        """
            we need to count all 1's in number
            in its binary representation when given
            its base-10 representation

            converting the base-10 to binary would
            be too annoying to implement

            recall that if a number is even, its
            least significant bit (LSB) is 0
            if it is odd, it is 1

            in otherwords, if n (mod 2) = 0, then
            the number in binary ends with a 0
            and 1 if n (mod 2) = 1

            IDEA (1)    get the modulo of the number
                        to get its LSB in binary
            
            IDEA (2)    if LSB is 1, add 1 to the
                        hamming weight 

            to remove the LSB of the number we
            can use right shifting

            IDEA (3)    use right shifting to remove
                        the LSB
            
            IDEA (4)    right shift n until n is <= 1

            IDEA (5)    add n to the counter at the end
        """
        ctr = 0 

        while n > 1:            # iterate until n is 0
            if (n % 2 == 1):    # since all odd numbers have 1 as their least significant bit (LSB)
                                # not having 1 as their LSB will make them an even number
                ctr += 1            # increment 1 in the counter if it is odd
            n = n // 2          # integer division of a number deletes the LSB  
                                # // is equal to right shifting

        return ctr + n