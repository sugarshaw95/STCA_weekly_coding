class Solution:
    def toLowerCase(self, str: str) -> str:
        new_s=''
        for i in range(len(str)):
            if ord('A')<=ord(str[i])<=ord('Z'):
                new_s+=(chr(ord(str[i])+32))
            else:
                new_s+=str[i]
        return new_s