class Solution:
    def reverseBits(self, n: int) -> int:
        bin_n=bin(n)
        bin_n='0'*(34-len(bin_n))+bin(n)[2:]
        return int('0b'+bin_n[::-1],2)
