# Problem 844.
# Backspacing String Compare.
from typing import List


class Solution:
    # While this function calculates the effective length of the string
    # it also moves all the characters at the start of the string
    # to use to do a comparison later
    # e.g. a#bc => acbc
    def getEffectiveLength(self, s: List[str]) -> int:
        length = 0
        for i in range(len(s)):
            if s[i] == '#':
                if length != 0:
                    length -= 1
            else:
                s[length] = s[i]
                length += 1
        return length

    def backspaceCompare(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        sLength = self.getEffectiveLength(s)
        tLength = self.getEffectiveLength(t)
        if sLength == tLength:
            if s[0:sLength] != t[0:sLength]:
                return False
            return True
        return False


if __name__ == '__main__':
    s = "ab#c"
    t = "ad#c"
    print("Input: s = " + s + " t = " + t)
    print("Output: " + str(Solution().backspaceCompare(s, t)))
    s = "ab##"
    t = "c#d#"
    print("Input: s = " + s + " t = " + t)
    print("Output: " + str(Solution().backspaceCompare(s, t)))
    s = "a#c"
    t = "b"
    print("Input: s = " + s + " t = " + t)
    print("Output: " + str(Solution().backspaceCompare(s, t)))
