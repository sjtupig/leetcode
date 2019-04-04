# Definition for singly-linked list.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    
        
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        #单调栈
        #单调栈
        def outstack(res, stack):
            t = stack.pop()
            
            if stack:
                res[t[0]] = stack[-1][1]
            else:
                res[t[0]] = 0
            return res, stack 
        nums = []
        stack = []
        res = {}
        while head:
            nums.append(head.val)
            head = head.next
        for i,v in enumerate(nums[::-1]):
            
            while stack and v >= stack[-1][1]:
                
                res,stack = outstack(res,stack)
            #这里可能由重复数据，所以把索引和数据一起存入栈，当然也可以只存索引，然后把nums作为参数传给函数通过索引取值
            stack.append((i,v))
        while stack:
            res,stack = outstack(res,stack)
        
        return [res[len(nums)-1-i] for i in range(len(nums))]#因为前面遍历数组是从后往前，所以原本的索引len(nums)-1变成了0，这里要恢复回去
        
        
head = ListNode(2);a = ListNode(7);c = ListNode(4);d=ListNode(3);e=ListNode(5)
head.next=a;a.next=c;c.next=d;d.next=e 
sol = Solution()
print(sol.nextLargerNodes(head))