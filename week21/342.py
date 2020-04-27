class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        s='01'*16
        return num > 0 and num & (num - 1) == 0 and num & int('0b'+s,2)!=0
		##前两项check是否为2的幂 后一个check 为1的那一位的位置(奇or偶)