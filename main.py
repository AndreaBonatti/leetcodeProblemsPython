# Problem 2849.
# Determine if a Cell is reachable at a Given Time.


class Solution:
    def isReachableAtTime(self, sx: int, sy: int, fx: int, fy: int, t: int) -> bool:
        if 0 <= t <= 10 ** 9:
            # If the 2 position are the same:
            # with one move, we can only go away from target.
            # Even for t == 0, it would be true as we would be at target without moving anywhere.
            # For t > 1, we can always come back to the cell.
            if sx == fx and sy == fy:
                return t != 1
            # Chebyshev_distance
            return max(abs(sx - fx), abs(sy - fy)) <= t
        else:
            return False


if __name__ == '__main__':
    sx = 1
    sy = 2
    fx = 1
    fy = 2
    t = 1
    print(f"Input: sx = {sx}, sy = {sy}, fx = {fx}, fy = {fy}, t = {t}")
    print(f"Output: {Solution().isReachableAtTime(sx, sy, fx, fy, t)}")
    sx = 2
    sy = 4
    fx = 7
    fy = 7
    t = 6
    print(f"Input: sx = {sx}, sy = {sy}, fx = {fx}, fy = {fy}, t = {t}")
    print(f"Output: {Solution().isReachableAtTime(sx, sy, fx, fy, t)}")
    sx = 3
    sy = 1
    fx = 7
    fy = 3
    t = 3
    print(f"Input: sx = {sx}, sy = {sy}, fx = {fx}, fy = {fy}, t = {t}")
    print(f"Output: {Solution().isReachableAtTime(sx, sy, fx, fy, t)}")
