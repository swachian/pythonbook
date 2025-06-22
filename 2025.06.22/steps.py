class Solution:
    def __init__(self):
        pass

    def climb_stairs(self, n):
        results = [0]
        for i in range(1, n+1):
            if i == 1:
                results.append(1)
            elif i == 2:
                results.append(2)
            else:
                results.append(results[i-2] + results[i-1])
        return results[-1]


solution = Solution()
print(solution.climb_stairs(2))

print(solution.climb_stairs(3))
print(solution.climb_stairs(4))
