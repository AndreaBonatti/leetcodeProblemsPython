# Problem 698.
# Partition to K Equal Sum Subsets.
from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        # If it is not possible divide the total in k parts without having a remainder
        # then we cannot have the k partitions
        if total % k != 0:
            return False
        subset_value = total // k
        subsets = [0] * k
        nums.sort(reverse=True)
        # The biggest number must be at least equal to the subset value
        if nums[0] > subset_value:
            return False

        def dfs(current_value: int, remaining_subsets: int, numbers: List[int]) -> bool:
            if current_value > subset_value:
                return False
            # A set is found
            if current_value == subset_value:
                remaining_subsets -= 1
                current_value = 0
            # If there are no more numbers in the original array and k is 0 we found the solution
            if not numbers:
                return not remaining_subsets
            # If there are more numbers we recursive call dfs
            for i in range(len(numbers)):
                if dfs(current_value + numbers[i], remaining_subsets, numbers[:i] + numbers[i + 1:]):
                    return True

        return dfs(0, k, nums)


if __name__ == '__main__':
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