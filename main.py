# Problem 2433.
# Find The Original Array of Prefix Xor.
from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        last = pref[0]
        result = [last]
        for element in pref[1:]:
            current = element ^ last
            result.append(current)
            last ^= current
        return result


if __name__ == '__main__':
    pref = [5, 2, 0, 3, 1]
    print("Input: pref = " + str(pref))
    print("Output: " + str(Solution().findArray(pref)))
    pref = [13]
    print("Input: pref = " + str(pref))
    print("Output: " + str(Solution().findArray(pref)))
