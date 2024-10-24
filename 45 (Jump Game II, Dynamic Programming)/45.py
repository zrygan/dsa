class Solution(object):
    def jump(self, nums):
        """
            we need to determine the minimum number of jumps
            
            IDEA (1):   dynamic programming
                        since we need to look for the minimum
                        number of jumps or the path of least cost
                        we can implement this as dynamic programming
                        
            issue with dynamic programming approach, we will need to
            pass through the array twice (from 0 to n and from i to n)
            
            this is O(n^2)
            
            we need to have a solution that is a single pass through, 
            getting the best solution while passing through the array
            
            IDEA (2):   greedy algorithm
                        since we are looking for the minimum cost
                        a greedy algorithm would also work
                        
            greedy algorithm:
                1. Initialize the current index (curr) to 0 and the farthest jump (farthest) to 0.
                2. Iterate through the array to determine how far you can jump from each index.
                3. When the loop reaches the curr index:
                    3.1 Increment the jump counter n_jumps.
                    3.2 Update curr to the farthest reachable index.
                    3.3 If curr reaches or exceeds the last index, break the loop.
        """            
        
        # base cases
        if len(nums) <= 1:
            return 0
        elif len(nums) == 2:
            return 1
        
        n_jumps = 0     # count of jumps made 
        curr = 0        # the current reachable index
        farthest = 0    # farthest index reachable from current position
        
        for i in range(len(nums) - 1):  
            farthest = max(farthest, i + nums[i])   # update farthest reachable index
                                                    # get max of the farthest
                                                    # and farthest of the current node
                                                    # given by index + value (i + nums[i])
            if i == curr:                           # if the loop reached the current farthest jump
                                                    # if we need to make a jump
                n_jumps += 1                        # increment the number of jumps
                curr = farthest                     # move to the farthest reachable index
                if curr >= len(nums) - 1:           # stop if out of bounds
                    break
        
        return n_jumps
