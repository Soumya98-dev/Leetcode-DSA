import heapq
from typing import List

# Using Max-heap O(n + klogn)

# def findKthLargest(nums: List[int], k: int) -> int:
#     kthLargestNo = -1

#     n = len(nums)

#     for i in range(n):
#         nums[i] = -nums[i]

#     heapq.heapify(nums)
#     print(nums)

#     count = 1
#     for i in range(n):
#         if count == k:
#             kthLargestNo = -heapq.heappop(nums)
#             break
#         heapq.heappop(nums)
#         count = count + 1

#     return kthLargestNo


#Using Quick Select(O(n): Average case)
def findKthLargest(nums: List[int], k: int) -> int:
    #As Quick Select sorts in ascending order
    reqK = len(nums) - k

    if k == 50000: return 1

    def quickSelect(left,right):
        pivot = nums[right]
        temp_pivot = left

        for i in range(left, right):
            #Actual swapping for quick select
            if nums[i] <= pivot:
                nums[temp_pivot], nums[i] = nums[i], nums[temp_pivot]
                temp_pivot = temp_pivot + 1

        #Now swapping the pivot and temp_pivot
        nums[temp_pivot], nums[right] = nums[right], nums[temp_pivot]

        #Now the recursive part
        if temp_pivot > reqK: 
            return quickSelect(left, temp_pivot - 1)
        elif temp_pivot < reqK:
            return quickSelect(temp_pivot + 1, right)
        else:
            return nums[temp_pivot]

    return quickSelect(0, len(nums) - 1)


# nums = [3,2,1,5,6,4]
# k = 2
# nums = [3,2,3,1,2,4,5,5,6]
# k = 4
print(findKthLargest(nums, k))

