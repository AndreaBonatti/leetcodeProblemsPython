# Problem 1446.
# Consecutive Characters.

class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        maxPower = 1
        temp = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                temp += 1
                if temp > maxPower:
                    maxPower = temp
            else:
                temp = 1

        return maxPower


if __name__ == '__main__':
    s = "cc"
    print("Input: s = " + s + " - Output: " + str(Solution().maxPower(s)))
    s = "leetcode"
    print("Input: s = " + s + " - Output: " + str(Solution().maxPower(s)))
    s = "abbcccddddeeeeedcba"
    print("Input: s = " + s + " - Output: " + str(Solution().maxPower(s)))
