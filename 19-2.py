# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        tmp = head
        list_len = 0
        while tmp:
            tmp = tmp.next
            list_len += 1
            
        if list_len == 1:
            return None

        if list_len - n == 0:
            return head.next

        tmp = head
        for i in range(list_len - n - 1):
            tmp = tmp.next
        
        tmp.next = tmp.next.next
        
        return head