/*
    Solution (1) by Zhean Ganituen (zrygan)
    For Leetcode #18
*/

#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target){
        /*
            we iterate through the array 4 times
            (a) will go [0 to n - 3]
            (b) will go [a to n - 2]
            (c) will go [b to n - 1]
            (d) will gp [d to n]

            1.  sort the array
            2.  check if the value at the current
                index for each iteration is not a duplicate
                since it is sorted checking A[i] == A[i - 1]
                will check if A[i] is a duplicate
            3.  for all non-duplicate values check if the sum
                of the four array indices is equal to the target

            IDEA:   brute-force solution
        */

        int n = nums.size(); 
        vector<vector<int>> quads;

        // base case
        if (n < 4) return quads;

        sort(nums.begin(), nums.end());

        for (int a = 0; a < n - 3; a++) {                                                   // iteration 1
            if (a > 0 && nums[a] == nums[a - 1]) continue;                                  // check for duplicates
    
            for (int b = a + 1; b < n - 2; b++) {                                           // iteration 2
                if (b > a + 1 && nums[b] == nums[b - 1]) continue;                          // check for duplicates
            
                for (int c = b + 1; c < n - 1; c++) {                                       // iteration 3
                    if (c > b + 1 && nums[c] == nums[c - 1]) continue;                      // check for duplicates
            
                    for (int d = c + 1; d < n; d++) {                                       // iteration 4
                        if (d > c + 1 && nums[d] == nums[d - 1]) continue;                  // check for duplicates
            
                        long long sum = (long long) nums[a] + nums[b] + nums[c] + nums[d];  // get the sum
                                                                                            // use typecasting to long long as it
                                                                                            // can be very large
            
                        if (sum == target) {                                                // if the sum is the target
                            quads.push_back({nums[a], nums[b], nums[c], nums[d]});          // add it to the resulting array
                        }
                    }
                }
            }
        }
        return quads;
    }
};
