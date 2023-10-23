# Problem 17.
# Letter Combinations of a Phone Number.
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitsToLetters = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        combinations = []
        for digit in digits:
            if len(combinations) == 0:
                combinations = digitsToLetters[digit]
            else:
                temp = []
                for letter in digitsToLetters[digit]:
                    for comb in combinations:
                        temp.append(comb + letter)
                combinations = temp

        return combinations


if __name__ == '__main__':
    digits = "23"
    print("Input: digits = \"" + digits + "\" - Output: " + str(Solution().letterCombinations(digits)))
    digits = ""
    print("Input: digits = \"" + digits + "\" - Output: " + str(Solution().letterCombinations(digits)))
    digits = "2"
    print("Input: digits = \"" + digits + "\" - Output: " + str(Solution().letterCombinations(digits)))
