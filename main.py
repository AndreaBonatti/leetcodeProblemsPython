# Problem 1361.
# Validate Binary Tree Nodes.
from typing import List


class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # 1) Check if every child has a unique parent
        parents = [-1] * n
        for i in range(n):
            if leftChild[i] != -1:
                if parents[leftChild[i]] == -1:
                    parents[leftChild[i]] = i
                else:
                    return False
            if rightChild[i] != -1:
                if parents[rightChild[i]] == -1:
                    parents[rightChild[i]] = i
                else:
                    return False
        # 2) Find the root
        root = -1
        for i in range(n):
            if parents[i] == -1:
                # There is only one root
                if root == -1:
                    root = i
                else:
                    return False
        # The root must exist
        if root == -1:
            return False
        # 3) Detect cycles
        visited = []
        toVisit = []
        toVisit.insert(0, root)
        while len(toVisit) != 0:
            node = toVisit.pop()
            if node in visited:
                return False
            visited.insert(0, node)
            if leftChild[node] != -1:
                toVisit.append(leftChild[node])
            if rightChild[node] != -1:
                toVisit.append(rightChild[node])
        return len(visited) == n


if __name__ == '__main__':
    n = 4
    leftChild = [1, -1, 3, -1]
    rightChild = [2, -1, -1, -1]
    print("Input: n = " + str(n) + " leftChild = " + str(leftChild) + " rightChild = " + str(rightChild))
    print("Output: " + str(Solution().validateBinaryTreeNodes(n, leftChild, rightChild)))
    n = 6
    leftChild = [1, -1, -1, 4, -1, -1]
    rightChild = [2, -1, -1, 5, -1, -1]
    print("Input: n = " + str(n) + " leftChild = " + str(leftChild) + " rightChild = " + str(rightChild))
    print("Output: " + str(Solution().validateBinaryTreeNodes(n, leftChild, rightChild)))
