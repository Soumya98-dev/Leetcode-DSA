import heapq
from typing import List

def lastStoneWeight(stones: List[int]) -> int:
    n = len(stones)

    #Max-heapify the array
    for i in range(n):
        stones[i] = -stones[i]

    heapq.heapify(stones)

    #now checking the stones
    while len(stones) >= 2:
        y = -heapq.heappop(stones)
        x = -heapq.heappop(stones)
        if x == y:
            continue
        else:
            diff = y - x
            heapq.heappush(stones, -diff)

    # print(stones)

    return -stones[0] if len(stones) <= n else 0

stones = [2,7,4,1,8,1]
print(lastStoneWeight(stones))


