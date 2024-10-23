"""
     Solution by Zhean Ganituen (zrygan)
     For Leetcode #69
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        """
            constaint: we cannot use math.sqrt()
            or fractional exponents

            recall 
                a^2 = x; sqrt(x) = a
                a * a = x; sqrt(x) = a

            we need to look for (SEARCH) for the
            value of a such that a * a = x since
            sqrt(x) = a.

            we can look through the entire set of possible
            numbers in 32-bit integers (1 to 2147483647)

            IDEA:   use a fast search algorithm
                    (binary search) to look for it
                    where start = 1 and 
                    end = 2147483647
        """

        # base case 
        if x == 0 or x == 1:
            return x
        
        start = 1
        end = 2147483647
        mid = 0
        while start <= end:
            mid = (start + end) // 2
            if mid * mid < x:
                start = mid + 1
            elif mid * mid > x:
                end = mid - 1
            else:
                return floor(mid)
        
        return floor(end)