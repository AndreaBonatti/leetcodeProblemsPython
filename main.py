# Problem 222.
# Count Complete Tree Nodes.
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

        def depthLeft(node: Optional[TreeNode]) -> int:
            depth = 0
            while node:
                depth += 1
                node = node.left
            return depth

        def depthRight(node: Optional[TreeNode]) -> int:
            depth = 0
            while node:
                depth += 1
                node = node.right
            return depth

        dl = depthLeft(root.left)
        dr = depthRight(root.right)

        # This condition has sense only for the specific requirement of the problem
        if dl == dr:
            return 2 ** (dl + 1) - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)


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
