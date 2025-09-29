class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
            # Heap

        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            first = -heapq.heappop(max_heap)  # sabse bada
            second = -heapq.heappop(max_heap) # dusra bada

            if first != second:
                heapq.heappush(max_heap, -(first - second))


        return -max_heap[0] if max_heap else 0



        # while len(stones) > 1:
        #     stones.sort()
        #     pile = stones[-1] - stones[-2]

        #     stones.pop()
        #     stones.pop()

        #     if pile != 0:
        #         stones.append(pile)


        # return stones[0] if stones else 0