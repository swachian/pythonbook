class Solution:
    def __init__(self):
        pass

    def climb_stairs(self, n):
        count = 0
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        count += self.climb_stairs(n - 2)
        count += self.climb_stairs(n-1)
        return count

solution = Solution()
print(solution.climb_stairs(2))

print(solution.climb_stairs(3))
print(solution.climb_stairs(4))
