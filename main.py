# Problem 111.
# Minimum Depth of Binary Tree.
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def walk(root: Optional[TreeNode]):
            if root.left is None and root.right is None:
                return 1
            if root.left and root.right is None:
                return 1 + walk(root.left)
            if root.left is None and root.right:
                return 1 + walk(root.right)
            if root.left and root.right:
                return min(1 + walk(root.left), 1 + walk(root.right))

        return walk(root) if root else 0


if __name__ == '__main__':
    root = TreeNode(
        3,
        TreeNode(9),
        TreeNode(
            20,
            TreeNode(15),
            TreeNode(7)
        )
    )
    print("Output: " + str(Solution().minDepth(root)))
    root = TreeNode(
        2,
        None,
        TreeNode(
            3,
            None,
            TreeNode(
                4,
                None,
                TreeNode(
                    5,
                    None,
                    TreeNode(6)
                )
            )
        )
    )
    print("Output: " + str(Solution().minDepth(root)))
