# 61. Rotate List
# Solved
# Medium
# Topics
# premium lock icon
# Companies
# Given the head of a linked list, rotate the list to the right by k places.

 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [4,5,1,2,3]


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None
        l=0
        dummy=head
        while dummy is not None:
                l+=1
                dummy=dummy.next
        k%=l
        for i in range(k):
            temp=head
            tail=temp
            prev=temp
            while tail.next is not None:
                prev=tail
                tail =tail.next
            tail.next=temp
            head=prev.next
            prev.next=None
        return head

