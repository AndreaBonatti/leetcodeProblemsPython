# Problem 1030.
# Matrix Cells in Distance Order
from typing import List


class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        cellsWithDistance = []
        for row in range(rows):
            for col in range(cols):
                distance = abs(row - rCenter) + abs(col - cCenter)
                cellsWithDistance.append({
                    "distance": distance,
                    "value": [row, col]
                })

        return [cell["value"] for cell in sorted(cellsWithDistance, key=lambda x: x["distance"])]


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
