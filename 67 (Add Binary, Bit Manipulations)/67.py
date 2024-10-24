"""
     Solution by Zhean Ganituen (zrygan)
     For Leetcode #27
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """
            since adding two numbers is from right to left
           
            IDEA (1):   reverse the 2 numbers

            adding two numbers depends on the largest (longest)
            number. Example, 123 + 12 is:
                123
                012 <- add a leading 0 since 12 is "shorter"
            
            IDEA (2):   determine which between the 2 numbers is
                        "longer"
            
            recall bit addition:
            case 1:     01 + 01 + 01 = 11 = 3 (base-10)
            case 2:     01 + 01 + 00 = 10 = 2 (base-10)
            case 3:     01 + 00 + 00 = 01 = 1 (base-10)

            IDEA (3):   notice when the sum is even, the LSB
                        (least significant bit) is 0

            IDEA (4):   also notice when the sum is odd, the
                        LSB is 1

            IDEA (5):   combining (3, 4), the sum of 2 numbers
                        under modulo 2 is the LSB of its 
                        base-2 representation

            For case 1 and 2, we have a carry value, notice that
            we know that we have a carry value if and only if
            the digit to the right of the LSB is 1

            IDEA (6):   the right shift of the sum is the carry
                        value

            example: 01 + 01 = 10 and right shift of 10 is 1,
            for 01 + 01 we do indeed have a carry value         
        """
        
        # base cases
        if a == "0" and b == "0":
            return "0"
        elif a == "1" and b == "0" or a == "0" and b == "0":
            return "1"
        elif a == "1" and b == "1":
            return "10"

        res = []
        car = 0

        # reverse a b
        a, b = a[::-1], b[::-1]
        
        # get the longest between the two numbers (as strings)
        max_len = len(a) if len(a) > len(b) else len(b)
        
        # add the two numbers digit by digit
        for i in range(max_len):
            # since we will loop through the "longest" number
            # we will go out-of-bounds for the "shorter" number
            # if the lengths are not equal
            # check if the current index is within bounds of that
            # string
            # if it is, set the value to the integer value of the 
            # current character 
            # otherwise, set it to 0
            bit_a = int(a[i]) if i < len(a) else 0
            bit_b = int(b[i]) if i < len(b) else 0

            sum = bit_a + bit_b + car
            
            # append the LSB of the sum to the result
            res.append(str(sum % 2))

            # get the carry through the right shift of the sum
            car = sum >> 1
        
        # if there's still a carry value, append it to the end
        if car:
            res.append(str(car))
        
        # return the reverse of the sum
        return "".join(res[::-1])