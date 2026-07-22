# 24. Swap Nodes in Pairs
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

# Example 1:

# Input: head = [1,2,3,4]

# Output: [2,1,4,3]

# Explanation:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp=head
        dummy=ListNode()
        prev=dummy
        prev.next=temp
        while temp is not None and temp.next is not None:
            mid=temp.next
            temp.next=temp.next.next
            mid.next=temp
            prev.next=mid
            prev=prev.next.next
            temp=temp.next
        return dummy.next