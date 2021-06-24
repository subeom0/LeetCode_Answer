# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def list2int(node):
            cnt, res = 1, 0
            while node:
                res += cnt*node.val
                node=node.next
                cnt*=10
            
            return res
        _sum = str(list2int(l1) + list2int(l2))
        
        node = None; prev = None
        
        for i in _sum:
            node = ListNode(i)
            node.next = prev
            prev = node
        
        return node
