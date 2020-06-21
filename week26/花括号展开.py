class S(set):
    def __add__(self, other):
        return S(self | other)
    
    def __mul__(self, other):
        return S(i + j for i, j in itertools.product(self, other))
    
class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        expression = re.sub('(\w+)', r'S(["\1"])', expression)
        d = {',': '+', '{': '(', '}': ')'}
        expression = re.sub('[\,\{\}]', lambda x: d[x.group(0)], expression)
        expression = re.sub('\)([S\(])', r')*\1', expression)
        return sorted(S(eval(expression)))