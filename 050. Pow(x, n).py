class Solution:
    def myPow(self, x, n):
        exp = abs(n)
        res = 1.0
        temp = x
        while exp:
            if exp & 1:
                res *= temp
            temp *= temp
            exp = exp >> 1
        return res if n > 0 else 1/res


sol = Solution()
print(sol.myPow(2.0,10))
print(sol.myPow(2.1,3))
print(sol.myPow(2.0,-2))