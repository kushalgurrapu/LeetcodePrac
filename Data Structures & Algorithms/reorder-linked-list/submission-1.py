# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        #now slow is at the midpoint of the list
        headTwo = slow.next
        slow.next = None
        #now we've split the list into two halves
        prev = None
        curr = headTwo
        while curr:
            nxt = curr.next
            curr.next = prev 
            prev = curr
            curr = nxt
        headTwo = prev
        #we've reversed the second half
        while headTwo:
            nxtOne = head.next
            head.next = headTwo
            nxtTwo = headTwo.next
            headTwo.next = nxtOne
            head = nxtOne
            headTwo = nxtTwo
        #merge the two halves now

