"""
    Solution by Zhean Ganituen (zrygan)
    For Leetcode #66
"""

class Solution(object):
    def plusOne(self, digits):
        """
            we have an array of numbers that represents each digit
            of the number
            123 -> [1,2,3]
            
            addition is from right to left so we reverse the array first
            
            IDEA (1):   reverse the array
            
            increment it digit-wise
            
            carry values are possible so we will get the ones digit of the sum
            and the carry value is the tens digit of the sum
            
            we can use modulo and right bit shifting to get the ones and tens digit
            
            IDEA (2):   use modulo and right shifting operators 
        """
        
        # reverse the array
        digits = digits[::-1]
        
        carry = 1
        
        for i in range(len(digits)):    # iternate through each digit
            sum = digits[i] + carry     # get the increment + carry
            digits[i] = sum % 10        # set digits as the ones digit of the sum
            carry = sum // 10           # set the carry as the tens digit of the sum
            
            if not carry:               # if there is no more carry values
                                        # then the digits onward will retain
                break                   # break
        
        # reverse again
        digits = digits[::-1]
        
        if carry:                       # if there's a carry
            digits.insert(0, carry)     # insert in front
            
        return digits