class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        n=len(weights)
        summ=sum(weights)
        def possible(weight):
            if weight<max(weights):
                return False
            elif weight>=summ:
                return True
            ##模拟过程,每一天尽可能多装 装不下了就留给下一天
            days=1
            cur=0
            for w in weights:
                if cur+w<=weight:
                    cur+=w
                else:
                    days+=1
                    cur=w
            ##看最后需要的天数是否<=D
            return days<=D

        ##二分查找范围

        low=max(weights)
        high=summ
        ##初始上下界
        while high-low>1:
            print(low,high)
            mid=(low+high)//2
            if possible(mid):

                high=mid
            else:
   
                low=mid
                

        return low if possible(low) else high