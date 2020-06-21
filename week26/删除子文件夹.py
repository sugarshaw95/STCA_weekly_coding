from collections import defaultdict
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        '''
        valid_folders=[]
        dicc=defaultdict(list)
        for f in folder:
            if f=='' or f=='/' or f.endswith('/'):
                continue
            path=tuple(f.split('/')[1:])
            dicc[len(path)].append(path)
        #valid_folders.sort(key=lambda x:len(x),reverse=True)
        #print(dicc)
        maxx=max(dicc.keys())
        def check(k,parents,path):
            #print(k,parents,path)
            for p in parents:
                if path[:k]==p:
                    return True
            return False
        keys=list(dicc.keys())
        for k in keys:
            if dicc[k]:
                for j in range(k+1,maxx+1):
                    if dicc[j]:
                        dicc[j]=[path for path in dicc[j] if not check(k,dicc[k],path)]
        ret=[]
        for k in dicc:
            for path in dicc[k]:
                ret.append('/'+'/'.join(path))
        '''
        ##字典序排序!!!! O(n)
        folder=sorted(folder)
        ret=[]
        parent=' '
        for path in folder:
            #print(parent)
            if not path.startswith(parent):
                ret.append(path)
                parent=path+'/'
                ##要加上一个/ 不然会出现例如 a/b/c 和a/b/ca这种情况

        return ret