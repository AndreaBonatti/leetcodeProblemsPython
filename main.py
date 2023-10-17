# Problem 14.
# Longest Common Prefix
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        # strings order by grammar e.g. flight, flow, flower
        sortedStrings = sorted(strs)
        first = sortedStrings[0]
        last = sortedStrings[-1]
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return prefix
            else:
                prefix += first[i]
        return prefix


if __name__ == '__main__':
    inputs = [["flower", "flow", "flight"], ["dog", "racecar", "car"]]
    for stringsArray in inputs:
        print("Input: " + str(stringsArray) + " Output: " + Solution().longestCommonPrefix(stringsArray))
