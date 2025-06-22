class Solution:
    def setZeroes(self, matrix) -> None:
        number_row = set()
        number_col = set()
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    number_row.add(i)
                    number_col.add(j)
        for n in number_row:
            for j in range(len(matrix[n])):
                matrix[n][j] = 0
        for n in number_col:
            for i in range(len(matrix)):
                matrix[i][n] = 0
        return matrix
        
solution = Solution()
print(solution.setZeroes([[1,1,1],[1,0,1],[1,1,1]]))