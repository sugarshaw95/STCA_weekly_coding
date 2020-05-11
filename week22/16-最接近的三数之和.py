class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()

        if target<=sum(nums[:3]):
            return sum(nums[:3])
        elif target>=sum(nums[-1:-4:-1]):
            return sum(nums[-1:-4:-1])        
        #小于最小或大于最大

        summ=sum(nums[:3])
        diff=target-summ
        ret=summ
        #初始化


        for i in range(len(nums)-2):
            #相当于双指针找target-nums[i]
            l=i+1
            r=len(nums)-1
            summ=nums[i]+nums[l]+nums[r]
            
            while l<r:
                #summ=sum(nums[l:r+1])
                #print(nums[i],nums[l],nums[r])
                if summ==target:
                    return summ
                if abs(target-summ)<diff:
                    diff=abs(target-summ)
                    ret=summ
                if summ<target:
                    summ-=nums[l]
                    l+=1
                    summ+=nums[l]
                    
                else:
                    summ-=nums[r]
                    r-=1
                    summ+=nums[r]
        return ret
