# Problem 3.
# Longest Substring Without Repeating Characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        # Map of the last seen position of a char
        seen = {}
        left = 0
        for right in range(len(s)):
            char = s[right]
            # If we found a char already seen we move the left pointer
            if char in seen and seen[char] >= left:
                left = seen[char] + 1
            else:
                # Every time we found a char not seen in the current substring we try to update the length
                length = max(length, right - left + 1)
            seen[char] = right
        return length


if __name__ == '__main__':
    inputs = ["abcabcbb", "bbbbb", "pwwkew"]
    for string in inputs:
        print("Input: \"" + string + "\" Output: " + str(Solution().lengthOfLongestSubstring(string)))
