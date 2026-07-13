# longest prefix
class Solution:
    def check(self,prefix,strs: List[str]) -> str:
        for m in range(len(strs)):
            if strs[m].startswith(prefix):
                continue
            else:
                return 0
        return 1

        
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word=strs[0]
        prefix=""
        fix2=""
        for i in word:
            prefix+=i
            if(self.check(prefix,strs)):
                pass
            else:
                prefix=fix2
                break 
            fix2=prefix
        return prefix


            #   altermnate soln
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        first=strs[0]
        last=strs[-1]
        i=0
        while i<len(first) and i<len(last) and first[i]==last[i]:
            i+=1
        return first[:i]
