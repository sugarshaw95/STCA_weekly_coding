class Solution:
    def reverseBits(self, n: int) -> int:
        bin_n=bin(n)
        bin_n='0'*(32-(len(bin_n)-2))+bin(n)[2:]
		#补齐32位
        return int('0b'+bin_n[::-1],2)
