class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        ret=0
        for n in s:
            #以n开始的序列
            if n-1 not in s:
            ##避免重复判断(因为Python会排好序 不然要设定一个访问记录) 
                nextt=n+1
                while nextt in s:
                    nextt+=1
                ret=max(ret,nextt-n)
        return ret
