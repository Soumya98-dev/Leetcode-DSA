# Algorithm

## Algo for formula approach

Count the frequencies of all tasks
Find the task with the maximum frequency
Formula for minimum time:
minimum time = (max_freq - 1) \* (n + 1) + number_of_tasks_with_max_freq

## Algo for heap approach

1. Count task freq
2. Push negated counts in the max heap (as Python only has min-heap)
3. While heap is not empty
   1. make a loop from i = 1 to n + 1
      1. pop the largest from the max-heap
      2. increment it by +1 (as it is negated)
      3. if it is < 0 push back into the heap (as unfinshed)
      4. keep track of the time
   2. If heap still has tasks remaining AND fewer than (n+1) tasks were run
      1. Add +1 idle time
