class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        '''
        res[0][0] = 0
        if n > 1 : res[0][1] = 1 
        if m > 1 : res[1][0] = 1 
        '''
        res = [[0]*n]*m
        for i in range(0,n):
        	res[0][i] = 1
        for i in range(0,m):
        	res[i][0] = 1
        for i in range(1,m):
        	for j in range(1,n):
        		t1 = res[i-1][j] if 0<= i-1 < m else 0
        		t2 = res[i][j-1] if 0<= j-1 < n else 0 
        		res[i][j] = t1+t2
        return res[m-1][n-1] 

'''机器人一定会走m+n-2步，即从m+n-2中挑出m-1步向下走不就行了吗？即C（（m+n-2），（m-1））。'''

sol = Solution()
print(sol.uniquePaths(7,3))
print(sol.uniquePaths(1,2))
print(sol.uniquePaths(2,1))
print(sol.uniquePaths(1,1))