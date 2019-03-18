class Solution:
    def searchRange(self, nums,target):
        #二分找到第一个、最后一个和target相等的元素位置
        l,r = 0, len(nums)-1
        res = []
        #找到最左边
        while l <= r:
            mid = (l+r)//2
            if nums[mid] >= target:#因为这里==target，r就会-1，最后nums[r]!=target，所以下面选取l
                r = mid-1
            else:
                l = mid+1
        if l < len(nums) and nums[l] == target:
            res.append(l)
        else:
            res.append(-1)
        #找最右边
        l,r = 0, len(nums)-1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] <= target:#因为这里==target，l就会+1，最后nums[l]!=target，所以下面选取r
                l = mid+1
            else:
                r = mid-1
        print(l,r)
        if r >= 0 and nums[r] == target:
            res.append(r)
        else:
            res.append(-1)
        return res 
class Solution:
    def searchRange(self, nums,target):
        if not nums:return [-1,-1]
        l,r = 0, len(nums)-1
        t = -1
        while l <= r:
            mid = (l+r)//2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                t = mid 
                break
        if t == -1:
            return [-1,-1]
        l = t
        while l >= 0 and nums[l] == target:
            l -= 1
        l+=1
        r = t
        while r < len(nums) and nums[r] == target:
            r += 1
        r -= 1
        return [l,r]
        
sol = Solution()
print(sol.searchRange([5,7,7,8,8,10],7))