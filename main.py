# Problem 779.
# K-th Symbol in Grammar.

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        halfRowLength = 2 ** (n - 2)
        if k > halfRowLength:
            return 1 if self.kthGrammar(n - 1, k - halfRowLength) == 0 else 0
        else:
            return self.kthGrammar(n - 1, k)


if __name__ == '__main__':
    n = 1
    k = 1
    print("Input: n = " + str(n) + ", k = " + str(k))
    print("Output: " + str(Solution().kthGrammar(n, k)))
    n = 2
    k = 1
    print("Input: n = " + str(n) + ", k = " + str(k))
    print("Output: " + str(Solution().kthGrammar(n, k)))
    n = 2
    k = 2
    print("Input: n = " + str(n) + ", k = " + str(k))
    print("Output: " + str(Solution().kthGrammar(n, k)))
