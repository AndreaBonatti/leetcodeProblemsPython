# Problem 2050.
# Parallel Courses III.
import copy
from typing import List, Dict


class Solution:

    def __init__(self):
        self.paths = []

    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:

        if n == 1:
            return time[0]
        if not relations:
            maxTime = 0
            for nodeTime in time:
                if maxTime < nodeTime:
                    maxTime = nodeTime
            return maxTime

        # Find the roots
        roots = []
        notRoots = []
        for relation in relations:
            possibleRoot = relation[0]
            notRoot = relation[1]
            if possibleRoot not in roots and possibleRoot not in notRoots:
                roots.insert(0, possibleRoot)
            if notRoot not in notRoots:
                notRoots.insert(0, notRoot)

        # Find the dictionary from the relations to use dfs
        adjecentDict = {}
        for i in range(1, n + 1):
            adjecentDict[i] = []
        for relation in relations:
            adjecentDict[relation[0]].append(relation[1])

        # Find the possible ends
        ends = []
        for node, links in adjecentDict.items():
            if not links:
                ends.append(node)

        # Find all the possible paths
        for root in roots:
            for end in ends:
                self.findAllPaths(adjecentDict, root, end)

        # Calculate the max time
        output = 0
        for path in self.paths:
            cost = 0
            for node in path:
                cost += time[node - 1]
            if cost > output:
                output = cost
        return output

    # This function uses DFS at its core to find all the paths in a graph
    def dfs(self, adjDict: Dict[int, List[int]], src: int, dst: int, path: List[int]):
        if src == dst:
            self.paths.append(copy.deepcopy(path))
        else:
            for node in adjDict[src]:
                path.append(node)
                self.dfs(adjDict, node, dst, path)
                path.pop()

    def findAllPaths(self, adjDict: Dict[int, List[int]], src: int, dst: int):
        path = [src]

        # Use depth first search (with backtracking) to find all the paths in the graph
        self.dfs(adjDict, src, dst, path)


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
