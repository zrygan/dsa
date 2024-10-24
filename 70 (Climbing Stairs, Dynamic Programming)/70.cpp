/*
    Solution by Zhean Ganituen (zrygan)
    For Leetcode #70
*/

class Solution {
public:
    int climbStairs(int n) {
        /*
            there are only two possible number of steps
            1 or 2

            so, before the n-th step, we must be at the
            (n - 1)-th or (n - 2)-th step.

            mathematically,
            F(n) = F(n - 1) + F(n - 1)

            IDEA:   this is the Fibonacci Sequence
                    implement this through Dynamic Programming
                    through Memoization to make it O(n)
        */
        
        // base cases
        if (n == 1) return 1;
        else if (n == 2) return 2;

        int dp[n];      // initialize an array with size n
        dp[0] = 1;      // base case n == 1
        dp[1] = 2;      // base case n == 2

        for (int i = 2; i < n; i++){
            dp[i] = dp[i - 2] + dp[i - 1];
        }
        
        return dp[n-1];
    }
};