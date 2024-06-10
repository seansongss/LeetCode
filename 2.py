from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        digit = 0
        sum = 0
        while l1 or l2:
            if l1:
                sum += l1.val * (10 ** digit)
                l1 = l1.next
            if l2:
                sum += l2.val * (10 ** digit)
                l2 = l2.next
            digit += 1
        
        if sum == 0:
            return ListNode()
        
        tmp = ListNode(sum % 10)
        res = tmp
        sum = sum // 10
        while sum:
            tmp.next = ListNode(sum % 10)
            sum = sum // 10
            tmp = tmp.next
        
        return res
        
print(Solution().addTwoNumbers(ListNode(2, ListNode(4, ListNode(3))), ListNode(5, ListNode(6, ListNode(4)))))