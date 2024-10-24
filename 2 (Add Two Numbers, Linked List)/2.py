# Definition for singly-linked list.
"""
     Solution by Zhean Ganituen (zrygan)
     For Leetcode #2
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
            we need to get the sum of two linked
            lists element-wise

            in addition we add from left to right
            so we should reverse the linked list
            but the linked list is already in reverse
            order

            we also cannot get the length of the linked
            list

            IDEA (1):   iterate through each linked list
                        until current node is None (null)
            
            since we will iterate through both linked
            lists at the same time, and each linked list
            may have a different size

            we need to check if the current node of that
            linked list is not none, and only if it is not
            then we will add it to the sum

            IDEA (2):   have a checker if the linked list
                        is not none, and we'll add the current
                        value only if not none

            we will need to handle carry values here, so
            the value that we set the the i-th element of the
            resultant linked list is the first digit of the sum
            of i-th element of linked list 1 and 2.

            we can get the first digit of any number through 
            the (mod 10) of the number

            IDEA (3):   get sum (mod 10) to get the digit

            then we can get the carry value by getting all values
            excluding the ones place, we can do this through
            dividing the sum by 10

            IDEA (4):   get carry value through sum // 10
                    
        """
        
        x = 0
        ln = ListNode()
        curr = ln

        # iterate through linked list until both are none
        while l1 or l2 or x:
            
            
            if l1:              # check if the element is not none
                x += l1.val     # add the current value to the sum
                l1 = l1.next    # move to the next element
            if l2:
                x += l2.val
                l2 = l2.next

            curr.next = ListNode(x % 10)    # set the element of the linked list
                                            # as the ones digit of the sum
            x //= 10                        # get all digits excluding the ones
                                            # set this as the carry
            curr = curr.next                # move to the next element of the 
                                            # resultant linked list

        return ln.next