# Problem 844.
# Backspacing String Compare.

class Solution:
    def getProcessedString(self, s: str):
        stack = []
        for char in s:
            if char == '#':
                if len(stack) != 0:
                    stack.pop()
            else:
                stack.append(char)
        return stack

    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.getProcessedString(s) == self.getProcessedString(t)


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
