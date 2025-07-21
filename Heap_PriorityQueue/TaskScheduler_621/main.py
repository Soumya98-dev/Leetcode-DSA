from typing import List
from collections import Counter
import heapq

"""
# * Formula App
def leastInterval(tasks: List[str], n: int) -> int:
    total_time = 0
    # * Counting the freq of all tasks
    freq = Counter(tasks)
    # * Task with the max freq
    max_freq = max(freq.values())
    # * No of tasks with max freq
    count_max_freq = 0
    for val in freq.values():
        # print(val)
        if val >= max_freq:
            count_max_freq = count_max_freq + 1
    # print(freq)
    # print(max_freq)
    # print(count_max_freq)
    # * Formula for minimum time
    minimum_element = (max_freq - 1) * (n + 1) + count_max_freq
    # * Total Time
    total_time = max(minimum_element, len(tasks))
    return total_time


# tasks = ["A", "A", "A", "B", "B", "B"]
# n = 2
tasks = ["A", "C", "A", "B", "D", "B"]
n = 1
print(leastInterval(tasks, n))
"""


# * Heap App
def leastInterval(tasks: List[str], n: int) -> int:
    # * Counting task freqs
    freq_count = Counter(tasks)
    # * Pushing negated counts into max-heap
    max_heap = []
    for val in freq_count.values():
        heapq.heappush(max_heap, -val)

    time = 0
    # * Checking if heap not empty
    while len(max_heap) != 0:
        temp_list = []
        cycle_time = 0
        # * Cycles starting
        for i in range(n + 1):
            # * popping the largest if heap not empty
            if max_heap:
                largest = heapq.heappop(max_heap)
                # * incrementing the largest by + 1 as negated b/c max-heap
                largest = largest + 1
                if largest < 0:
                    temp_list.append(largest)
                cycle_time = cycle_time + 1
            else:
                if len(temp_list) > 0:
                    cycle_time = cycle_time + 1
                else:
                    break

        for item in temp_list:
            heapq.heappush(max_heap, item)

        if max_heap and temp_list:
            time += (n + 1)
        else:
            time += cycle_time

    # print(max_heap)
    return time


# tasks = ["A", "A", "A", "B", "B", "B"]
# n = 2
# tasks = ["A", "C", "A", "B", "D", "B"]
# n = 1
tasks = ["A", "A", "B"]
n = 1
print(leastInterval(tasks, n))
