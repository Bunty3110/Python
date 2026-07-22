# 23. Merge k Sorted Lists
# Solved
# Hard
# Topics
# premium lock icon
# Companies
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Merge all the linked-lists into one sorted linked-list and return it.

 

# Example 1:

# Input: lists = [[1,4,5],[1,3,4],[2,6]]
# Output: [1,1,2,3,4,4,5,6]
# Explanation: The linked-lists are:
# [
#   1->4->5,
#   1->3->4,
#   2->6
# ]
# merging them into one sorted linked list:
# 1->1->2->3->4->4->5->6



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        k=len(lists)
        total=[]
        for i in range(k):
            temp=lists[i]
            while temp is not None:
                total.append(temp.val)
                temp=temp.next
        total=sorted(total)
        dummy=ListNode(0)
        temp=dummy
        for i in range(len(total)):
            temp.next=ListNode(total[i])
            temp=temp.next
        return dummy.next


        