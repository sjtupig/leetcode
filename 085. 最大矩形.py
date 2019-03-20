class Solution:
    def maximalRectangle(self, maps):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        def maxrecfrombotom(height):
            #对每个高度往左扩展，找到第一个小于它的高度的索引,单调增栈
            stack = []
            maxarea = 0
            for i,v in enumerate(height):
                while stack and v <= height[stack[-1]]:
                    t = stack.pop()
                    k = -1 if not stack else stack[-1]
                    cur = (i-1-k)*height[t]
                    maxarea = max(maxarea, cur)
                stack.append(i)
            while stack:
                t = stack.pop()
                k =-1 if not stack else stack[-1]
                maxarea = max(maxarea, (len(height)-1-k)*height[t])
            return maxarea
        if not maps:return 0
        m,n = len(maps), len(maps[0])
        height = [0]*n
        res = 0 
        for i in range(m):
            for j in range(n):
                height[j] = height[j]+1 if maps[i][j] == '1' else 0
            res = max(res, maxrecfrombotom(height))
        return res 