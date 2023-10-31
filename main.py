# Problem 833.
# Find And Replace in String.
from typing import List


class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        # iterate from the greater index to the smallest
        for i, src, tg in sorted(list(zip(indices, sources, targets)), reverse=True):
            # if found the pattern matches with the source, replace with the target accordingly
            if s[i:i+len(src)] == src: s = s[:i] + tg + s[i+len(src):]
        return s


if __name__ == '__main__':
    s = "abcd"
    indices = [2, 2]
    sources = ["cde","cdef"]
    targets = ["fe","f"]
    print("Inputs:")
    print("s = " + s)
    print("indices = " + str(indices))
    print("sources = " + str(sources))
    print("targets = " + str(targets))
    print("Output: " + str(Solution().findReplaceString(s, indices, sources, targets)))
    s = "abcd"
    indices = [0, 2]
    sources = ["a", "cd"]
    targets = ["eee", "ffff"]
    print("Inputs:")
    print("s = " + s)
    print("indices = " + str(indices))
    print("sources = " + str(sources))
    print("targets = " + str(targets))
    print("Output: " + str(Solution().findReplaceString(s, indices, sources, targets)))
    s = "abcd"
    indices = [0, 2]
    sources = ["ab", "ec"]
    targets = ["eee", "ffff"]
    print("Inputs:")
    print("s = " + s)
    print("indices = " + str(indices))
    print("sources = " + str(sources))
    print("targets = " + str(targets))
    print("Output: " + str(Solution().findReplaceString(s, indices, sources, targets)))
