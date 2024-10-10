# Ganituen, Zhean (zrygan)
# Solution (2) to problem 169

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()                     # sort the array
        return nums[len(nums) // 2]     # since the majority element should appear more than n / 2
                                        # the median is always the majority element