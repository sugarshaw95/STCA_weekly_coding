class Solution:
    def findMin(self, nums: List[int]) -> int:
        def bin_search(s,e):
            #print(s,e)
            if e<s:
                return -1
            if e-s<=1:
                return min(nums[s],nums[e])
            if nums[s]<nums[e]:
            #说明已经进入单调区间,直接返回
                return nums[s]
            mid=(s+e)//2

            ##因为旋转 会产生一个峰谷和峰底(最大和最小)
            #if nums[mid-1]>nums[mid] and nums[mid+1]>=nums[mid]:
                #mid是峰底
            #    return nums[mid]
            #elif nums[mid-1]<nums[mid] and nums[mid+1]<nums[mid]:
                #mid是峰谷,则峰底在前一个
            #    return nums[mid+1]
            #判断在右边还是左边
            if nums[mid]<nums[s]:
                #右边
                return bin_search(s,mid)
            elif nums[mid]>nums[s]:
                #左边
                return bin_search(mid,e)
            else:
                #有可能在左也有可能在右,把s左移1(safe策略)
                #while nums[s]==nums[mid]:
                #    pass
                return bin_search(s+1,e)
        return bin_search(0,len(nums)-1)