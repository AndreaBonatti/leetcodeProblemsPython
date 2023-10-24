# Problem 515.
# Find Largest Value in Each Tree Row.
from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # empty tree
        if not root:
            return []

        # BFS
        result = []
        queue = deque([root])

        while queue:
            level_nodes_number = len(queue)
            # Initial value -infinite
            max_value = -float('inf')

            for _ in range(level_nodes_number):
                node = queue.popleft()
                max_value = max(max_value, node.val)

                # Add the children node to the queue (ignored in this for because we consider the level_nodes_number)
                for child in [node.left, node.right]:
                    if child:
                        queue.append(child)

            result.append(max_value)

        return result


if __name__ == '__main__':
    # root = [1, 3, 2, 5, 3, null, 9]
    root = TreeNode(
        1,
        TreeNode(
            3,
            TreeNode(5),
            TreeNode(3)
        ),
        TreeNode(
            2,
            None,
            TreeNode(9)
        )
    )
    print("Input: root = " + str(root))
    print("Output: " + str(Solution().largestValues(root)))
    # root = [1,2,3]
    root = TreeNode(
        1,
        TreeNode(2),
        TreeNode(3)
    )
    print("Input: root = " + str(root))
    print("Output: " + str(Solution().largestValues(root)))
