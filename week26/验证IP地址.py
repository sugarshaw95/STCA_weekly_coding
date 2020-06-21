class Solution:
    def validIPAddress(self, IP: str) -> str:
        def check4(addr):
            if addr=='':
                return False
            for c in addr:
                if not c.isdigit():
                    return False
            if 0<=int(addr)<=255:
                if len(addr)>1 and addr[0]=='0':
                    return False
                return True
            return False
        def check6(addr):
            if len(addr)>4:
                return False
            for c in addr:
                if c.isdigit():
                    continue
                elif c.isalpha():
                    if not (ord('a')<=ord(c)<=ord('f') or ord('A')<=ord(c)<=ord('F')):
                        return False
                else:
                    return False
            return True
                        

        if '.' in IP:
            addrs=IP.split('.')
            if len(addrs)!=4:
                return 'Neither'
            for addr in addrs:
                if not check4(addr):
                    return 'Neither'
            return 'IPv4'
        else:
            addrs=IP.split(':')
            #print(addrs)
            if len(addrs)!=8:
                return 'Neither'
            for addr in addrs:
                if addr=='':
                    return 'Neither'
                if not check6(addr):
                    #print(addr)
                    return 'Neither'
            return 'IPv6' 