# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head.next:
            return None
        node, prev = head, None
        length = 0
        while node:
            length += 1
            node = node.next
        
        node = head
        if n==length:
            return head.next
        else:
            for _ in range(length-n):
                prev, node = node, node.next
            prev.next = node.next
            return head
