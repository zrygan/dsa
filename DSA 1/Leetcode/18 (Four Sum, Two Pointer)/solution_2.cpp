/*
    Solution (2) by Zhean Ganituen (zrygan)
    For Leetcode #18
*/

#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        /*
            solution (1) is very slow, O(n^4) since it iterates through
            the array four times

            instead of iterating through it four times we can only do it 
            twice to make it O(n^2)

            since the array is sorted we know that at some index i
            all elements to the left of i (i - x) will be small values
            while all elements to the right of i (i + x) will be large values

            with this, the current value of the two for loops will be held
            constant and we will have two indices that will adjust to the two
            current values such that their sum will be the target

            IDEA: two-pointer solution

            we will have two pointers:
            k for the smaller number
            l for the larger number

            if the sum > target, make l smaller by moving it left
            if the sum < target, make k larger by moving it right
         */

        int n = nums.size();
        vector<vector<int>> quads;
        
        // base case
        if (n < 4) return quads;
        
        sort(nums.begin(), nums.end());
        
        for (int i = 0; i < n - 3; ++i) {                                               // iteration 1
            if (i > 0 && nums[i] == nums[i - 1]) continue;                              // check for duplicates
            
            for (int j = i + 1; j < n - 2; ++j) {                                       // iteration 2
                if (j > i + 1 && nums[j] == nums[j - 1]) continue;                      // check for duplicates
                
                
                int k = j + 1;                                                          // first pointer (small number)
                int l = n - 1;                                                          // second pointer (large number)
                
                while (k < l) {                                                         // while k and l are not equal
                                                                                        // and the small number is less than the large number
                    long long x = (long long) nums[i] + nums[j] + nums[k] + nums[l];    // get the sum
                    
                    if (x < target) ++k;                                                // if the sum is smaller than the target
                                                                                        // move small number to the right 
                                                                                        // to make the sum bigger
                    else if (x > target) --l;                                           // if the sum is larger than the target
                                                                                        // move larger number to the left
                                                                                        // to make the sum smaller
                    
                    else {                                                              // if the sum is equal to the target
                        quads.push_back({nums[i], nums[j], nums[k++], nums[l--]});      // add the sum to the resulting array
                        while (k < l && nums[k] == nums[k - 1]) ++k;                    // skip duplicates for both pointers
                        while (k < l && nums[l] == nums[l + 1]) --l; 
                    }
                }
            }
        }
        return quads; 
    }
};
