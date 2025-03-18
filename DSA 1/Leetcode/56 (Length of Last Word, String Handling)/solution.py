"""
    Solution by Zhean Ganituen (zrygan)
    For Leetcode #56
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
            we can simply get an array of words from the string that
            is separated by a space ' '
            
            IDEA (1)    convert string to array of words for each element
                        in the array is a substring enclosed by ' '
            
            issue, this will also take "   " as a string in since it is a
            space enclosed by two spaces
            
            IDEA (2)    only include the word in the array of words
                        if it is not a ' ' or a space character
                        
            using array indexing from the right, we can get the length of the
            right most element of the array of words
            
            IDEA (3)    using array indexing from the right, get the length of the
                        right most element in the array of words
        """
        
        return len([word for word in s.split(' ') if word != ''][-1])
