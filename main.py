# Problem 342.
# Power of four.
import math


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # If 'n' is 1, it is a power of four
        if n == 1:
            return True
        # If 'n' is non-positive, it cannot be a power of four
        elif n <= 0:
            return False

        # Calculate the logarithm of 'n' with base 4
        logarithm_base4 = math.log(n) / math.log(4)

        # Check if the result of the logarithmic operation is an integer
        return logarithm_base4 == int(logarithm_base4)


if __name__ == '__main__':
    inputs = [16, 5, 1]
    for n in inputs:
        print("Input: n= " + str(n) + " Output: " + str(Solution().isPowerOfFour(n)))
