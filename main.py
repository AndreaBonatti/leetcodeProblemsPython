# Problem 1759.
# Count Number of Homogenous Substrings.


class Solution:
    def countHomogenous(self, s: str) -> int:
        counter = 0
        left = 0
        for right in range(len(s)):
            # if the left and right characters are the same we add the length of the string from left to right
            if s[left] == s[right]:
                counter += right - left + 1
            else:
                # counter increased by 1 for the new character, we move the left pointer because this is a new character
                counter += 1
                left = right
        return counter % (10 ** 9 + 7)


if __name__ == '__main__':
    inputs = ["abbcccaa", "xy", "zzzzz"]
    for s in inputs:
        print(f"Input: s = {s}")
        print(f"Output: {Solution().countHomogenous(s)}")
