# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        curr = head
        fast = head.next
        while fast:
            if (curr.val == fast.val):
                return True
            curr = curr.next
            if fast.next:
                fast = fast.next.next
            else:
                return False
        return False