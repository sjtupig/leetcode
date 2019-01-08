class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        #丢弃开头空格
        str = str.lstrip()
        nums = []
        if not str:return 0 
        signed = 1
        i = 0
        #先判断首字符是否是正负号
        if str[0] == '-':
        	signed = -1
        	i += 1
        elif str[0] == '+':
        	i += 1
        while i < len(str) and str[i] in ['0','1','2','3','4','5','6','7','8','9']:
        	nums.append(int(str[i]))
        	i += 1
        if not nums:return 0
        res = 0
        for i in nums:
        	res = res*10 + i
        if -2**31 > signed*res:
        	return -2**31
        elif signed*res > 2**31-1:
        	return 2**31-1
        else:
        	return signed*res 

sol = Solution()
print(sol.myAtoi("42"))
print(sol.myAtoi("   -42"))
print(sol.myAtoi("4193 with words"))
print(sol.myAtoi("words and 987"))
print(sol.myAtoi("-91283472332"))


#正则表达式解法
import re
class Solution2:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        try:
            res = re.match('^[\+\-]?\d+', str).group()
            res = int(res)
            res = res if res <= 2147483647 else 2147483647
            res = res if res >= -2147483648 else -2147483648
        except:
            return 0
        return res

sol2 = Solution2()
print(sol2.myAtoi("42"))
print(sol2.myAtoi("   -42"))
print(sol2.myAtoi("4193 with words"))
print(sol2.myAtoi("words and 987"))
print(sol2.myAtoi("-91283472332"))