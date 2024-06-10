from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        node_len = 0
        tmp = head
        while tmp:
            node_len += 1
            tmp = tmp.next

        if node_len == 1:
            return None
        if node_len == n:
            return head.next

        node_len -= (n + 1)

        tmp = head
        tmp_next = head.next
        while node_len > 0:
            tmp = tmp_next
            tmp_next = tmp.next
            node_len -= 1
        
        tmp.next = tmp_next.next

        return head
    
print(Solution().removeNthFromEnd(ListNode(1, ListNode(2)), 2).val)