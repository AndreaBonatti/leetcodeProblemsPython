# Problem 1356.
# Sort Integers by The Number of 1 Bits
from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def numbers_of_ones(number: int):
            return sum((number >> i) & 1 for i in range(32)), number

        return sorted(arr, key=lambda number: numbers_of_ones(number))


if __name__ == '__main__':
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    print("Input: arr = " + str(arr))
    print("Output: " + str(Solution().sortByBits(arr)))
    arr = [1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
    print("Input: arr = " + str(arr))
    print("Output: " + str(Solution().sortByBits(arr)))
