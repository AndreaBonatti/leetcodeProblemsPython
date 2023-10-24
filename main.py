# Problem 222.
# Count Complete Tree Nodes.
from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # empty tree
        if not root:
            return 0

        queue = deque([root])
        result = 0

        # BFS
        while queue:
            level_nodes_number = len(queue)

            for _ in range(level_nodes_number):
                node = queue.popleft()
                result += 1

                # Add the children node to the queue (ignored in this for because we consider the level_nodes_number)
                for child in [node.left, node.right]:
                    if child:
                        queue.append(child)

        return result


if __name__ == '__main__':
    root = TreeNode(
        1,
        TreeNode(
            2,
            TreeNode(4),
            TreeNode(5)
        ),
        TreeNode(
            3,
            TreeNode(6),
            None
        )
    )
    print(str(Solution().countNodes(root)))
    root = None
    print(str(Solution().countNodes(root)))
    root = TreeNode(1)
    print(str(Solution().countNodes(root)))
