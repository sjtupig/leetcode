#动态规划解参见：https://blog.csdn.net/linhuanmars/article/details/24506703
class Solution:
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if not s1 or not s2 or (len(s1)!=len(s2)):return False
        res = [[[False for _ in range(len(s1)+1)] for _ in range(len(s1))] for _ in range(len(s1))]
        for i in range(len(s1)):
        	for j in range(len(s2)):
        		res[i][j][1] = s1[i] == s2[j]
        
        for l in range(2, len(s1)+1):
        	for i in range(len(s1)-l+1):
        		for j in range(len(s1)-l+1):
        			for k in range(1,l):
        				res[i][j][l] = res[i][j][l] | (res[i][j][k] & res[i+k][j+k][l-k]) | (res[i][j+l-k][k] & res[i+k][j][l-k])
        return res[0][0][len(s1)]



class Solution3:
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2):return False
        a = ''.join(sorted(s1))
        b = ''.join(sorted(s2))
        if a != b:
            return False
        if len(s1) == 1:
        	return s1 == s2
        for i in range(1, len(s1)):
        	#未交换
            if self.isScramble(s1[i:], s2[i:]) and self.isScramble(s1[:i], s2[:i]):
                return True
            #交换
            if self.isScramble(s1[i:], s2[:-i]) and self.isScramble(s1[:i], s2[-i:]):
                return True
        return False

class Solution3:
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if len(s1) != len(s2):return False
        a = ''.join(sorted(s1))
        b = ''.join(sorted(s2))
        if a != b:
            return False
        if len(s1) == 1:
        	return s1 == s2
        for mid in range(1, len(s1)):
        	t = s2[len(s1[mid:]):]+s2[:len(s1[mid:])]
        	if (self.isScramble(s1[:mid],s2[:mid]) and self.isScramble(s1[mid:],s2[mid:])) or (self.isScramble(s1[:mid],t[:mid]) and self.isScramble(s1[mid:],t[mid:])):
        		return True 
        return False







class Solution2:
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        #如果以长度来二分，就可以这么写
        if len(s1) != len(s2):return False
        l = len(s1)
        mid = int(l/2)

        if l == 1: 
        	return s1 == s2 
        t = s2[len(s1[mid:]):]+s2[:len(s1[mid:])]
        return (self.isScramble(s1[:mid],s2[:mid]) and self.isScramble(s1[mid:],s2[mid:])) or (self.isScramble(s1[:mid],t[:mid]) and self.isScramble(s1[mid:],t[mid:]))

sol = Solution()
print(sol.isScramble(s1 = "great", s2 = "rgeat"))
print(sol.isScramble(s1 = "abcde", s2 = "caebd"))
print(sol.isScramble(s1 = "abb", s2 = "bba"))
print(sol.isScramble(s1 = "abb", s2 = "bab"))
print(sol.isScramble(s1 = "bab", s2 = "abb"))

