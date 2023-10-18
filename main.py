# Problem 2050.
# Parallel Courses III.
import copy
from collections import defaultdict, deque
from typing import List, Dict


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        # Build the graph and calculate in-degrees
        graph = defaultdict(list)
        in_degree = [0] * (n + 1)
        for u, v in relations:
            graph[u].append(v)
            in_degree[v] += 1

        # Initialize the dist array and queue
        dist = [0] + time
        queue = deque([i for i in range(1, n + 1) if in_degree[i] == 0])

        # Perform Topological Sort
        while queue:
            course = queue.popleft()
            for next_course in graph[course]:
                dist[next_course] = max(dist[next_course], dist[course] + time[next_course - 1])
                in_degree[next_course] -= 1
                if in_degree[next_course] == 0:
                    queue.append(next_course)

        return max(dist)


if __name__ == '__main__':
    n = 3
    relations = [[1, 3], [2, 3]]
    time = [3, 2, 5]
    print("Input: n = " + str(n) + ", relations = " + str(relations) + ", time = " + str(time))
    print("Output: " + str(Solution().minimumTime(n, relations, time)))
    n = 5
    relations = [[1, 5], [2, 5], [3, 5], [3, 4], [4, 5]]
    time = [1, 2, 3, 4, 5]
    print("Input: n = " + str(n) + ", relations = " + str(relations) + ", time = " + str(time))
    print("Output: " + str(Solution().minimumTime(n, relations, time)))
    n = 7
    relations = [[1, 7], [1, 4], [1, 3], [2, 3], [4, 3], [5, 3], [7, 3], [7, 6]]
    time = [6, 5, 1, 8, 2, 9, 4]
    print("Input: n = " + str(n) + ", relations = " + str(relations) + ", time = " + str(time))
    print("Output: " + str(Solution().minimumTime(n, relations, time)))
