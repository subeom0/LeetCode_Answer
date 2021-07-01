# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = '',''
        while l1:
            s1 += str(l1.val)
            l1 = l1.next
        while l2:
            s2 += str(l2.val)
            l2 = l2.next
        
        _sum = str(int(s1) + int(s2))
        
        cnt, node, tmp = True, None, None
        head = None
        for i in _sum:
            if cnt:
                cnt = False
                node = ListNode(i)
                head = node
            else:
                tmp = node
                node = ListNode(i)
                tmp.next = node
        
        return head
