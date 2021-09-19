class Solution(object):
    def longestCommonPrefix1(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) <2:
            return strs[0]
        
        pre = ""
        v = strs[0]
        i=0
        

        while i<len(v):
            for j in strs:
                if v[i] != j[i:i+1]:
                    return pre
            pre += v[i]
            i += 1
        
        return pre
    
        
test = Solution()
s = ["flower", "flwe", "flo"]
print(test.longestCommonPrefix(s))