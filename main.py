# Problem 26.
# Remove Duplicates from Sorted Array
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        counter = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[counter] = nums[i]
                counter += 1
        return counter


if __name__ == '__main__':
    inputs = [[1, 1, 2], [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]]
    for array in inputs:
        print("Input: " + str(array) + " Output: " + str(Solution().removeDuplicates(array)))
