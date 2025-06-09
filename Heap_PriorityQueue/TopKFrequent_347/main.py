from typing import List
from collections import Counter
import heapq

#Hashmap + Sorting App
# def topKFrequent(nums: List[int], k: int) -> List[int]:
#     counter = Counter(nums)

#     new_counter = sorted(counter.items(), key = lambda x: x[1], reverse=True)

#     # print(new_counter)

#     res = []
#     count_k = 0
#     for ele, count in enumerate(new_counter):
#         if count_k == k:
#             break
#         res.append(new_counter[ele][0])
#         count_k = count_k + 1

#     return res
#     # return []


#Hashmap + Heap
# def topKFrequent(nums: List[int], k: int) -> List[int]:
#     #Counting frequencies with counter
#     counter = Counter(nums)

#     # print(counter)

#     #min-heap to keep track of the top k elements based on frequency
#     min_heap = []

#     for key, val in counter.items():
#         if len(min_heap) < k:
#             heapq.heappush(min_heap, (val, key))
#         else:
#             heapq.heappushpop(min_heap, (val, key))


#     return [h[1] for h in min_heap]
#     # return []


#Hashmap + Bucket Sort
def topKFrequent(nums: List[int], k: int) -> List[int]:
    counter = Counter(nums)
    n = len(nums)

    #initializing a bucket for storing the frequencies
    bucket = [0] * (n+1)

    #putting the elements in the bucket based on the frequency
    for val,freq in counter.items():
        if bucket[freq] == 0:
            bucket[freq] = [val]
        else:
            bucket[freq].append([val])

    #Looping through the end of the bucket to find the top k frequent elements
    res = []
    for item in range(n, -1, -1):
        if bucket[item] != 0:
            res.extend(bucket[item])
        if len(res) == k:
            break


    return res




nums = [1,1,1,2,2,3]
k = 2

print(topKFrequent(nums, k))


