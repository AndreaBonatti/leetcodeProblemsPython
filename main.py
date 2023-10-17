# Problem 4.
# Median of Two Sorted Arrays
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3 = self.mergeTwoSortedArrays(nums1, nums2)
        index = int(len(nums3) / 2)
        if len(nums3) % 2:
            # Even
            return nums3[index]
        else:
            # Odd
            return (nums3[index - 1] + nums3[index]) / 2

    def mergeTwoSortedArrays(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i = 0  # iterator for nums1
        j = 0  # iterator for nums2
        k = 0  # iterator for nums3
        lenNums1 = len(nums1)
        lenNums2 = len(nums2)
        nums3 = [None] * (lenNums1 + lenNums2)

        # traverse both arrays
        while i < lenNums1 and j < lenNums2:
            if nums1[i] < nums2[j]:
                nums3[k] = nums1[i]
                i = i + 1
            else:
                nums3[k] = nums2[j]
                j = j + 1
            k = k + 1
        # Store remaining elements
        while i < lenNums1:
            nums3[k] = nums1[i]
            i = i + 1
            k = k + 1
        while j < lenNums2:
            nums3[k] = nums2[j]
            j = j + 1
            k = k + 1

        return nums3


if __name__ == '__main__':
    nums1 = [1, 3]
    nums2 = [2]
    print("Nums1: " + str(nums1) + " Nums2: " + str(nums2) + " Median: " +
          str(Solution().findMedianSortedArrays(nums1, nums2)))
