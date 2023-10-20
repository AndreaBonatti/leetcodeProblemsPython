# Problem 27.
# Remove Element.
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[length] = nums[i]
                length += 1
        return length


if __name__ == '__main__':
    nums = [3, 2, 2, 3]
    val = 3
    print("Input: " + str(nums) + ", val= " + str(val))
    length = Solution().removeElement(nums, val)
    print("Output: " + str(length) + " val = " + str(nums[0:length]))
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    val = 2
    print("Input: " + str(nums) + ", val= " + str(val))
    length = Solution().removeElement(nums, val)
    print("Output: " + str(length) + " val = " + str(nums[0:length]))
