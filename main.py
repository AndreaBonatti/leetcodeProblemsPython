# Problem 1921.
# Eliminate Maximum Number of Monsters.
from typing import List


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        # Ordering the monsters by the arrival time to the city
        arrival_time = [dist[i] / speed[i] for i in range(len(dist))]
        arrival_time.sort()
        for i in range(len(arrival_time)):
            if arrival_time[i] <= i:
                return i
        return len(dist)


if __name__ == '__main__':
    dist = [1, 3, 4]
    speed = [1, 1, 1]
    print(f"Input: dist = {dist}, speed = {speed}")
    print(f"Output: {Solution().eliminateMaximum(dist, speed)}")
    dist = [1, 1, 2, 3]
    speed = [1, 1, 1, 1]
    print(f"Input: dist = {dist}, speed = {speed}")
    print(f"Output: {Solution().eliminateMaximum(dist, speed)}")
    dist = [3, 2, 4]
    speed = [5, 3, 2]
    print(f"Input: dist = {dist}, speed = {speed}")
    print(f"Output: {Solution().eliminateMaximum(dist, speed)}")
