'''
需用到辅助数组d[s.length()]，表示从当前字符开始，到字符串结尾的最长有效括号子串长度（当前字符需为有效括号子串的第一个字符）

解题思路：从字符串结尾往前处理，求辅助数组d[]

当前字符下标为index，若当前字符为左括号'('，判断index+1+d[index+1]位置的字符是否为右括号')'，若为右括号，则d[index] = d[index+1]+2，并且判断index+1+d[index+1]+1位置的元素是否存在，若存在，则d[index] += d[index+1+d[index+1]+1]（解决上述两个有效括号子串直接相邻的情况）

'''
class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        now_longest_length = [0] * len(s)#初始化为0，这样求()的时候可以不用另外再单独讨论
        res = 0 
        for i in range(len(s)-2, -1, -1):
        	if s[i] == '(':
        		if i+1+now_longest_length[i+1] < len(s) and s[i+1+now_longest_length[i+1]] == ')':
        			now_longest_length[i] = now_longest_length[i+1]+2
        			if i+1+now_longest_length[i+1]+1 < len(s):
        				now_longest_length[i] += now_longest_length[i+1+now_longest_length[i+1]+1]

        	res = max(res, now_longest_length[i])
        return res 


sol = Solution()
print(sol.longestValidParentheses('(()'))
print(sol.longestValidParentheses(')()())'))
print(sol.longestValidParentheses(')((()()(((())))))'))


'''

解题思路：
 
1.需有一个变量start记录有效括号子串的起始下标，max表示最长有效括号子串长度，初始值均为0
 
2.遍历给字符串中的所有字符
 
    2.1若当前字符s[index]为左括号'('，将当前字符下标index入栈（下标稍后有其他用处），处理下一字符
 
    2.2若当前字符s[index]为右括号')'，判断当前栈是否为空
 
        2.2.1若栈为空，则start = index + 1，处理下一字符（当前字符右括号下标不入栈）
 
        2.2.2若栈不为空，则出栈（由于仅左括号入栈，则出栈元素对应的字符一定为左括号，可与当前字符右括号配对），判断栈是否为空
 
            2.2.2.1若栈为空，则max = max(max, index-start+1)
 
            2.2.2.2若栈不为空，则max = max(max, index-栈顶元素值)
'''