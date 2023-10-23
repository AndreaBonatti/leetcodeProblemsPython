# Problem 32.
# Longest Valid Parentheses.

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        output = 0
        stack = [-1]
        for index, char in enumerate(s):
            if char == "(":
                stack.append(index)
            else:
                stack.pop()
                if stack:
                    output = max(output, index - stack[-1])
                else:
                    stack.append(index)

        return output


if __name__ == '__main__':
    inputs = ["()(()", "(()", ")()())", ""]
    for string in inputs:
        print("Input: s= \"" + string + "\"")
        print("Output: " + str(Solution().longestValidParentheses(string)))
