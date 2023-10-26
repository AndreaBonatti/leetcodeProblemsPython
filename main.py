# Problem 258.
# Add Digits.

class Solution:
    # The idea:
    # xyz = 100*x + 10*y + z = x + y + z + (99*x + 9*y) = x + y + z + 9*(11*x + 1*y)
    # => xyz(mod 9) = (x + y + z + 9*(11*x + 1*y))(mod 9) = x + y + z
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        elif num % 9 == 0:
            return 9
        else:
            return num % 9


if __name__ == '__main__':
    for num in [38, 0]:
        print("Input: num = " + str(num))
        print("Output: " + str(Solution().addDigits(num)))
