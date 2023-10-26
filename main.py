# Problem 823.
# Binary Trees With Factors.
from typing import List


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        # The dictionary contains the number of binary tree starting from a specific node as root
        # We start with one tree for every node that is made only by a single node
        dct = {item: 1 for item in arr}
        for root in arr:
            for factor in arr:
                # If we reach the same node we stop because the array is sorted
                # if we continue we only find bigger nodes that could not be leaves for new tree
                if factor == root:
                    break
                # If root is divisible by the selected factor
                # and the result of division is the dictionary === is in the array
                # Then we add the new trees in the array
                if root % factor == 0 and root // factor in dct:
                    # It works like this because we sort the array at the start
                    dct[root] += dct[factor] * dct[root // factor]

        return sum(dct.values()) % (pow(10, 9) + 7)


if __name__ == '__main__':
    arr = [2, 4]
    print("Input: arr = " + str(arr))
    print("Output: " + str(Solution().numFactoredBinaryTrees(arr)))
    arr = [2, 4, 5, 10]
    print("Input: arr = " + str(arr))
    print("Output: " + str(Solution().numFactoredBinaryTrees(arr)))
