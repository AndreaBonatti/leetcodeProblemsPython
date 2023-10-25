# Problem 1737.
# Change Minimum Characters to Satisfy One of Three Conditions.
import sys
from collections import Counter


class Solution:
    def minCharacters(self, a: str, b: str) -> int:
        n, m = len(a), len(b)
        aCount, bCount = Counter(a), Counter(b)
        # maxLetter = max(max(aCount), max(bCount))

        def change(map1: dict, map2: dict):
            answer = sys.maxsize
            op1 = sum(map1.values())
            op2 = 0

            for letter in "abcdefghijklmnopqrstuvwxy":
                op1 -= map1[letter]
                op2 += map2[letter]
                answer = min(answer, op1 + op2)
                # if letter == maxLetter:
                #     break
            return answer

        cond1 = change(aCount, bCount)
        cond2 = change(bCount, aCount)
        cond3 = n + m - max(aCount.values()) - max(bCount.values())

        return min(cond1, cond2, cond3)


if __name__ == '__main__':
    a = "da"
    b = "cced"
    print("Input: a = \"" + a + "\" b =\"" + b + "\"")
    print("Output: " + str(Solution().minCharacters(a, b)))
    # a = "dcada"
    # b = "d"
    # print("Input: a = \"" + a + "\" b =\"" + b + "\"")
    # print("Output: " + str(Solution().minCharacters(a, b)))
    # a = "ace"
    # b = "abe"
    # print("Input: a = \"" + a + "\" b =\"" + b + "\"")
    # print("Output: " + str(Solution().minCharacters(a, b)))
    # a = "bddae"
    # b = "abbb"
    # print("Input: a = \"" + a + "\" b =\"" + b + "\"")
    # print("Output: " + str(Solution().minCharacters(a, b)))
    # a = "da"
    # b = "cced"
    # print("Input: a = \"" + a + "\" b =\"" + b + "\"")
    # print("Output: " + str(Solution().minCharacters(a, b)))
    # a = "dee"
    # b = "a"
    # print("Input: a = \"" + a + "\" b =\"" + b + "\"")
    # print("Output: " + str(Solution().minCharacters(a, b)))
    # a = "aba"
    # b = "caa"
    # print("Input: a = \"" + a + "\" b =\"" + b + "\"")
    # print("Output: " + str(Solution().minCharacters(a, b)))
    # a = "dabadd"
    # b = "cda"
    # print("Input: a = \"" + a + "\" b =\"" + b + "\"")
    # print("Output: " + str(Solution().minCharacters(a, b)))
