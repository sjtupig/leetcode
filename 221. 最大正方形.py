class Solution:
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        #因为正方形可以以角点和边长确定，索引记录以每个点做右下角点的正方形的边长，扩展的时候，点i,j 和i-1,j;i,j-1;i-1,j-1的边长有关
        if not matrix: return 0
        m,n = len(matrix), len(matrix[0])
        res = [[0 for _ in range(n)] for _ in range(m)]
        r = 0
        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0) and int(matrix[i][j]) == 1: 
                    res[i][j] = 1
                    r = max(r, res[i][j])
                elif i and j and int(matrix[i][j]) == 1:
                    res[i][j] = min(res[i-1][j], res[i][j-1], res[i-1][j-1])+1
                    r = max(r, res[i][j])
        return r*r
                
                    
sol = Solution()
print(sol.maximalSquare([[1, 0, 1, 0, 0],
                         [1, 0, 1, 1, 1],
                         [1, 1, 1, 1, 1],
                         [1, 0, 0, 1, 0]]))
print(sol.maximalSquare([["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))