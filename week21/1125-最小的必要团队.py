class Solution:
    def smallestSufficientTeam(self, req_skills, people) :
        n=len(req_skills)
        skill2i={}
        for i in range(n):
            skill2i[req_skills[i]]=i
        
        bitmasks={}
        for i in range(len(people)):
            bitmask=0
            for skill in people[i]:
                bitmask|=1<<skill2i[skill]
            bitmasks[i]=bitmask
        

        m=len(people)
 
        dp=[ [-1 for k in range(m+1)] for j in range(1<<n)] 
        #for j in range(1<<n):
        #    dp[j]=[0] if bitmasks[0]&j==j else [-1 for k in range(m+1)]
        dp[0]=[]

        for i in range(m):
            bitmask=bitmasks[i]

            for j in (range(1<<n)):
              
                
                if bitmask|j!=j:
                    if len(dp[j])+1<len(dp[bitmask|j]):
                        dp[j|bitmask]=dp[j]+[i]

        return dp[(1<<n)-1]