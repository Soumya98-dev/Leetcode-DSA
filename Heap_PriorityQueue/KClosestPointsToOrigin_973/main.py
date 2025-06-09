from typing import List
from collections import defaultdict
import heapq

#Sorting + Hashmap App(O(nlogn))
# def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
#     #d(x,y) = x^2 + y^2

#     n = len(points)
#     dist_points_hashmap = defaultdict(list)
#     print(dist_points_hashmap)

#     #Calculating the distances
#     for i in range(n):
#         dist = points[i][0] * points[i][0] + points[i][1] * points[i][1]
#         x = points[i][0]
#         y = points[i][1]
#         dist_points_hashmap[dist].append([x,y])

#     print(dist_points_hashmap)

#     #Sorting the distance hashmap based on the keys
#     sorted_distances = sorted(dist_points_hashmap.keys())

#     print(sorted_distances)

#     #Using the sorted dist_points_hashmap and matching the value 'k' times
#     n = len(sorted_distances)
#     res = []

#     for i in range(n):
#         res.extend(dist_points_hashmap[sorted_distances[i]])
#         if len(res) == k:
#             break

#     return res

#Heap (O(logk))
def kClosest(points: List[List[int]], k: int) -> List[List[int]]:
    def distance(x,y):
        return x**2 + y**2

    max_heap = []
    n = len(points)

    for x, y in points:
        dist = distance(x,y)
        if len(max_heap) < k:
            heapq.heappush(max_heap, (-dist, x, y))
        else:
            heapq.heappushpop(max_heap, (-dist, x, y))


    return [[x,y] for d, x, y in max_heap]



# points = [[1,3],[-2,2]] 
points = [[3,3], [2,2], [4,4], [1,1]]
k = 2

print(kClosest(points, k))

