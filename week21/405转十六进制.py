class Solution:
    def toHex(self, num: int) -> str:
        num &= 0xFFFFFFFF
        s = "0123456789abcdef"
        res = ""
        mask = 0xF
        while num > 0:
            res = s[num & mask]+res
            num >>= 4
        return res if res else "0"