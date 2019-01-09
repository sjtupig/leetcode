'''
解题思路参考
https://blog.csdn.net/baodream/article/details/80417695
'''
class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """

        #res = [[0]*n]*m,不要用这种初始化方法，因为每一列的元素同时变化
        m, n = len(word1)+1, len(word2)+1
        res = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            res[i][0] = i
        for i in range(n):
            res[0][i] = i
        #print(res)
     
        for i in range(1,m):
        	for j in range(1, n):
        		flag = 1 if word1[i-1] != word2[j-1] else 0
        		res[i][j] = min(res[i-1][j]+1, res[i][j-1]+1, res[i-1][j-1]+flag)

        return res[m-1][n-1]

sol = Solution()
print(sol.minDistance("horse","ros"))
print(sol.minDistance("intention","execution"))
print(sol.minDistance("michaelab","michaelxy"))

