from collections import list

#Sorting approach: O(nlgn)
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        sorted_nums = sorted(nums)

    def add(self, val: int) -> int:
        nums.append(val)
        sorted_nums = sorted(nums)
        return sorted_nums[self.k-1]







KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2])
print(kthLargest.add(3)) 