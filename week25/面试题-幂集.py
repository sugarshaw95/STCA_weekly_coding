class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        if n==0:
            return []
        if n==1:
            return [[],[nums[0]]]
        #ret=[]
        cur=[()]
        #cur=self.subsets(nums[1:])
        for i in range(n):
            nextt=[]
            for e in cur:
                nextt.append(tuple([nums[i]])+e )
                nextt.append(e)
            cur=nextt


        return list(set(cur))
