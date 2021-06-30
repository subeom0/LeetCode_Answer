# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        _list = []
        
        for i in lists:
            while i:
                _list.append(i.val)
                i = i.next
        
        _list.sort()
        cnt, node, tmp = True, None, None
        head = None
        for i in _list:
            if cnt:
                cnt = False
                node = ListNode(i)
                head = node
            else:
                tmp = node
                node = ListNode(i)
                tmp.next = node
        
        return head
