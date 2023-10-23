# Problem 6.
# Zigzag Conversion.

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [[] for _ in range(numRows)]
        rowIndex = 0
        # +1 => go down, -1 go up
        step = 1
        for char in s:
            rows[rowIndex].append(char)
            # Change step direction when we reach the top or bottom row
            if rowIndex == 0:
                step = 1
            elif rowIndex == numRows - 1:
                step = -1
            rowIndex += step

        for i in range(numRows):
            rows[i] = "".join(rows[i])
        return ''.join(rows)


if __name__ == '__main__':
    numRows = 3
    string = "PAYPALISHIRING"
    print("Input: s = \"" + string + "\" numRows = " + str(numRows) +
          " - Output: " + str(Solution().convert(string, numRows)))
    numRows = 4
    string = "PAYPALISHIRING"
    print("Input: s = \"" + string + "\" numRows = " + str(numRows) +
          " - Output: " + str(Solution().convert(string, numRows)))
    numRows = 1
    string = "A"
    print("Input: s = \"" + string + "\" numRows = " + str(numRows) +
          " - Output: " + str(Solution().convert(string, numRows)))
