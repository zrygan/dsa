/*
    Solution by Zhean Ganituen (zrygan)
    For Leetcode #1
*/

#include <vector>
#include <algorithm> // For std::sort

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        /*
            We can simply iterate through the loop twice
            adding the i-th + j-th element. But this is 
            O(n^2)

            1. Make an array of the original indices and values
            2. Sort the elements O(n log n)
            3. iterate through the array from 0 to n O(n)
            4. get the sum = A.start + A.end
                4.1 if sum > target, move end to the left
                    (decrease the sum)
                4.2 if sum < target, move start to the right
                    (increase the sum)

            IDEA:   two-pointer method and divide-and-conquer
                    this is O(n) 
        */
        
        // Create an array that contains an ordered pair
        // (original index , value)
        std::vector<std::pair<int, int>> indexed;

        for (int i = 0; i < nums.size(); ++i) {
            indexed.emplace_back(nums[i], i);
        }

        // sort the array
        std::sort(indexed.begin(), indexed.end());

        // output array
        std::vector<int> res;

        // initialize the two-pointers
        int start = 0;
        int end = indexed.size() - 1;

        // two-pointer technique
        while (start < end) {

            // if the sum of the start and end elements
            int sum = indexed[start].first + indexed[end].first;

            if (sum == target) {
                res.push_back(indexed[start].second);   // original index of the left number
                res.push_back(indexed[end].second);     // original index of the right number
                return res;

            } 
            else if (sum < target) ++start;           // move start to the right
            else --end;                               // move end to the left
        }

        return res; 
    }
};
