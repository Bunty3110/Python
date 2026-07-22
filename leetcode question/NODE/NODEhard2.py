# 25. Reverse Nodes in k-Group
# Solved
# Hard
# Topics
# premium lock icon
# Companies
# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

# You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

# Example 1:


# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
# Example 2:


# Input: head = [1,2,3,4,5], k = 3
# Output: [3,2,1,4,5]



class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return None

        tail = head

        for _ in range(k):
            if not tail:
                return head
            tail = tail.next

        def reverse(cur, end):
            prev = None

            while cur != end:
                next = cur.next
                cur.next = prev
                prev = cur
                cur = next

            return prev      

        new_head = reverse(head, tail)
        head.next = self.reverseKGroup(tail, k)

        return new_head            