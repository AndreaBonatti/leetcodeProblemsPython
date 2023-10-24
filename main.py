# Problem 1030.
# Matrix Cells in Distance Order
from typing import List


class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        def distance(cell: [int, int]) -> int:
            return abs(cell[0] - rCenter) + abs(cell[1] - cCenter)

        cells = [[row, col] for row in range(rows) for col in range(cols)]
        return sorted(cells, key=distance)


if __name__ == '__main__':
    rows = 1
    cols = 2
    rCenter = 0
    cCenter = 0
    print("Input: rows = " + str(rows) + " cols = " + str(cols)
          + " rCenter = " + str(rCenter) + " cCenter = " + str(cCenter))
    print("Output: " + str(Solution().allCellsDistOrder(rows, cols, rCenter, cCenter)))
    rows = 2
    cols = 2
    rCenter = 0
    cCenter = 1
    print("Input: rows = " + str(rows) + " cols = " + str(cols)
          + " rCenter = " + str(rCenter) + " cCenter = " + str(cCenter))
    print("Output: " + str(Solution().allCellsDistOrder(rows, cols, rCenter, cCenter)))
    rows = 2
    cols = 3
    rCenter = 1
    cCenter = 2
    print("Input: rows = " + str(rows) + " cols = " + str(cols)
          + " rCenter = " + str(rCenter) + " cCenter = " + str(cCenter))
    print("Output: " + str(Solution().allCellsDistOrder(rows, cols, rCenter, cCenter)))
