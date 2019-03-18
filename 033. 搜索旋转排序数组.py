class Solution:
    def search(self, nums, target):
        if not nums:return -1
        l,r = 0, len(nums)-1
        targetAtleft = target >= nums[0]
        while l <= r:
            mid = (l+r)//2
            if target == nums[mid]:
                return mid
            atleftHalf = nums[mid] >= nums[0]
            if targetAtleft == atleftHalf:
                #都在左半区间的时候就是正常的二分搜索，或者都在右半区间的时候
                if target > nums[mid]:
                    l = mid+1
                elif target < nums[mid]:
                    r = mid-1
            elif not targetAtleft and atleftHalf:
                #target在右半区间，而mid在左半区间，往右调整
                l = mid+1
            else:
                r = mid-1
        return -1

sol = Solution()
print(sol.search([4,5,6,7,0,1,2],10))