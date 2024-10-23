/*
    Solution by Zhean Ganituen (zrygan)
    For Leetcode #27
*/

int removeElement(int* nums, int numsSize, int val) {
    /*

        We need to get all elements that is not val
        in the first k values of the array

        Such that, A = [1,2,3,1,1] (val = 1)
        will return 2 and A[0:2] = [2,3]

        So, we will not make a new array, only
        edit the current array (this is known as 
        in-place)

        IDEA:   have a counter of elements that is not
                equal to val
    */

    // counter for elems not equal to val
    int k = 0;

    for (int i = 0; i < numsSize; i++){ // iterate through the array
        if (nums[i] != val){            // if nums[i] is not val
            nums[k] = nums[i];          // let the k-th elem be nums[i]
            k++;                        // increment i
                                        // this will remove all elems equal to val
                                        // at the first k elems of the array
                                        // elems at index m > k doesn't matter 
        }
    }

    return k;
}