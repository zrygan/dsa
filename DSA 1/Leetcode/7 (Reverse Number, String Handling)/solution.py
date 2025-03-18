"""
     Solution by Zhean Ganituen (zrygan)
     For Leetcode #7
"""

class Solution(object):
    def reverse(self, x: int) -> int:
        """
            we cannot "flip" an integer around
            but we can "flip" a string around through
            slicing
            
            IDEA (1):   convert the int to a string 

            but we cnnt flip the number if it is negative
            since "-12" (flip) "21-"

            what we can do is remove and save the sign of the
            int, then convert to a string for flipping

            to remove the sign of the number, recall same sign
            removes the sign (+) * (+) = (+) and (-) * (-) = (+)
            
            so, by multiplying the number with its own sign we retrieve
            its unsigned (positive) number equivalent            
            
            IDEA (2):   store the sign of the number and
                        remove the sign the number before
                        converting the number to a string

            finally, we need to check if the flipped number is still
            in the bounds of a 32-bit integer. 1999999999 (flip)
            9999999991 which is out of bounds.

            IDEA (3):   check if the number is still within bounds
        """
        
        # get and store the sign of the number
        negative = -1 if x < 0 else 1
        
        # remove the sign of the number
        x *= negative
        
        # convert it to string
        # then flip through slicing
        # then convert back to int
        x = int(str(x)[::-1])
        
        # check if out-of-bounds
        if x > 2147483647:
            return 0

        # return the number multiplied to its original sign
        return x * negative