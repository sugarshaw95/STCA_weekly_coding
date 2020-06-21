class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        #一个set 两个dic 对于元音 转换成忽略元音的小写字符 然后映射()
        word_set=set(wordlist)
        word_dic={}
        yuanyin_dic={}
        yuanyins={'a','e','i','o','u'} 
        def yuanyin_p(s):
            return ''.join(['*' if c in 'aeiou' else c for c in list(s)])
        ##把元音替换成*  
        for w in wordlist:
            if w.lower() not in word_dic:
                word_dic[w.lower()]=w
            yuanyin_w=yuanyin_p(w.lower())
            if yuanyin_w not in yuanyin_dic:
                yuanyin_dic[yuanyin_w]=w


        answers=[]
        for q in queries:
            if q in word_set:
                answers.append(q)
                continue
            q=q.lower()
            if q in word_dic:
                answers.append(word_dic[q])
                continue
            if set(q)|yuanyins:
                yuanyin_q=yuanyin_p(q)
                if yuanyin_q in yuanyin_dic:
                    answers.append(yuanyin_dic[yuanyin_p(q)])
                else:
                    answers.append('')
        return answers