class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        heap = []
        for num in freq:
            if len(heap) < k:
                heapq.heappush(heap, (freq[num], num))
            elif freq[num] > heap[0][0]:
                heapq.heapreplace(heap, (freq[num], num))
        return [x[1] for x in heap]