class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        heap = []

        for i, val in enumerate(nums):
            heapq.heappush(heap, (val, i))
            if len(heap) > k:
                heapq.heappop(heap)

        heap.sort(key=lambda x: x[1])

        return [val for val, idx in heap]

        # res = []

        # for i in range(len(nums)):
        #     res.append((nums[i],i))

        # res.sort(reverse=True)

        # topk = res[:k]

        # topk.sort(key=lambda x: x[1])

        # arr = []
        # for val,idx in topk:
        #     arr.append(val)

        # return arr