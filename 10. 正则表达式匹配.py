class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not s and not p:
        	return True 
        elif s and not p:
        	return False 
        elif not s and p:
        	if len(p) > 1 and p[1] == '*':
        		return self.isMatch(s, p[2:])
        	else:
        		return False
        elif len(p) > 1 and p[1] == '*':
        	if s[0] != p[0] and p[0] != '.':
        		return self.isMatch(s,p[2:])
        	else:
        		return self.isMatch(s,p[2:]) or self.isMatch(s[1:], p) or self.isMatch(s[1:],p[2:])
        else:
        	if s[0] == p[0] or p[0] == '.':
        		return self.isMatch(s[1:], p[1:])
        	else:return False

sol = Solution()
print(sol.isMatch("aa", "a"))
print(sol.isMatch("aa", "a*"))
print(sol.isMatch("a", "a*"))
print(sol.isMatch("ab", ".*"))
print(sol.isMatch("aab", "c*a*b"))
print(sol.isMatch("mississippi", "mis*is*p*."))
print(sol.isMatch("bbbba", ".*a*a"))
print(sol.isMatch("aaaaaaaaaaaaab","a*a*a*a*a*a*a*a*a*a*c"))