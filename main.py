# Problem 698.
# Partition to K Equal Sum Subsets.
from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        # If it is not possible divide the total in k parts without having a remainder
        # then we cannot have the k partitions
        if total % k:
            return False

        subset_value = total // k
        subsets = [0] * k
        nums.sort(reverse=True)

        def dfs(curr: int) -> bool:
            if curr == len(nums):
                return True
            for i in range(k):
                if subsets[i] + nums[curr] <= subset_value:
                    subsets[i] += nums[curr]
                    if dfs(curr + 1):
                        return True
                    subsets[i] -= nums[curr]
                    if subsets[i] == 0:
                        break
            return False

        return dfs(0)


if __name__ == '__main__':
    nums = [2, 2, 2, 2, 3, 4, 5]
    k = 4
    print("Input: nums= " + str(nums) + " k = " + str(k))
    print("Output: " + str(Solution().canPartitionKSubsets(nums, k)))
    nums = [4, 3, 2, 3, 5, 2, 1]
    k = 4
    print("Input: nums= " + str(nums) + " k = " + str(k))
    print("Output: " + str(Solution().canPartitionKSubsets(nums, k)))
    nums = [1, 2, 3, 4]
    k = 3
    print("Input: nums= " + str(nums) + " k = " + str(k))
    print("Output: " + str(Solution().canPartitionKSubsets(nums, k)))
    nums = [3, 3, 10, 2, 6, 5, 10, 6, 8, 3, 2, 1, 6, 10, 7, 2]
    k = 6
    print("Input: nums= " + str(nums) + " k = " + str(k))
    print("Output: " + str(Solution().canPartitionKSubsets(nums, k)))
