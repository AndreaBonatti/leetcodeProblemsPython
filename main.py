# Problem 9.
# Given an integer x, return true if x is a palindrome, and false otherwise.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        strNumber = str(x)
        return strNumber == strNumber[::-1]


if __name__ == '__main__':
    inputs = [121, -121, 10]
    for input in inputs:
        print("Input: " + str(input) + " Output: " + str(Solution().isPalindrome(input)))
