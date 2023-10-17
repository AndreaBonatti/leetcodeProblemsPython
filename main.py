# Problem 20.
# Valid Parenthesis.

class Solution:
    def isValid(self, s: str) -> bool:
        # stack of opening parenthesis
        stack = []
        for parenthesis in s:
            if parenthesis == "(" or parenthesis == "[" or parenthesis == "{":
                stack.append(parenthesis)
            else:
                if (
                        not stack or
                        (stack[-1] == "(" and parenthesis != ')') or
                        (stack[-1] == "[" and parenthesis != ']') or
                        (stack[-1] == "{" and parenthesis != '}')
                ):
                    return False
                stack.pop()
        return len(stack) == 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    inputs = ["()", "()[]{}", "(]"]
    for string in inputs:
        print("Input: " + string + " Output: " + str(Solution().isValid(string)))
