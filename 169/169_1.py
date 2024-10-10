# Ganituen, Zhean (zrygan)
# Solution (1) to problem 169

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ctr = 0             # counter
        elem = -1           # the majority element
        
        for i in nums:      # loop through each element
            if ctr == 0:        # if the counter is 0
                elem = i        # set the ith number as elem
                ctr = 1         # set counter to 1
            elif elem == i: # else if elem is ith nums
                ctr += 1        # increment counter
            else:           # else
                ctr -= 1        # decrement counter

        return elem