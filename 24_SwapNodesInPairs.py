# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
#         node = head
        
#         while node and node.next:
#             node.val, node.next.val = node.next.val, node.val
#             node = node.next.next
            
#         return head
        
        if head and head.next:
            p = head.next
            head.next = self.swapPairs(p.next)
            p.next = head
            return p
        
        return head
