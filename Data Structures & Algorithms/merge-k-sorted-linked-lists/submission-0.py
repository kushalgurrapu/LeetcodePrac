# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        counter = 0
        for head in lists:
            if head:
                heapq.heappush(heap, (head.val, counter, head))
                counter += 1
        if not heap:
            return None
        head = heap[0][2]
        while heap:
            curr = heapq.heappop(heap)
            if curr[2].next:
                nxt = curr[2].next
                heapq.heappush(heap, (nxt.val, counter, nxt))
                counter += 1
            if heap:
                curr[2].next = heap[0][2]
        return head

            
        