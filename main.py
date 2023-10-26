# Problem 258.
# Add Digits.

class Solution:
    def addDigits(self, num: int) -> int:
        return num if num <= 9 else self.addDigits(sum([int(i) for i in str(num)]))


if __name__ == '__main__':
    for num in [38, 0]:
        print("Input: num = " + str(num))
        print("Output: " + str(Solution().addDigits(num)))
