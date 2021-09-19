class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        i=0
        j=0
        len_p = len(p)
        len_s = len(s)
        # Check if pattern ends with spl char
        while True:
            if j==len_p and i==len_s:
                return True
            elif j==len_p and i<len_s:
                return False
            elif j<len_p and i==len_s:
                return False
            
            if p[j] not in ['.', '*']:
                # p=".a*b*" s="abb" This should match
                # '.' and 'a' will match.
                # 'a' and 'b' will not match
                #  |-- Check if the next patt is '*'. If YES, next iteration. If NO, return FALSE
                if s[i] != p[j]:
                    if (j==len_p) or p[j+1] != '*': 
                        return False
                    if (j+1 < len_p) and p[j+1]=='*':
                        j += 1
                        i -= 1
                i += 1
                j += 1
            
            elif p[j] == '.':
                i += 1
                j += 1

            elif p[j] == '*':  # ma(n)* and mannnnn
                
                if p[j-1] != '.':
                    while  s[i] == p[j-1]:
                        i += 1
                        if i==len_s:
                            # p="a*a" s="aaa"
                            while j+1< len_p:
                                j += 1
                                if s[i-1] != p[j]:
                                    return False
                            break
                    j +=1
                elif p[j-1] == '.':
                    # If pattern ends with '.*' return TRUE
                    if j == len_p-1: 
                        return True
                    
                    # Look for the next character
                    while p[j] in ['.', '*']:
                        j += 1
                        if j==len_p: # Reached EOP and no 'ch'.  TRUE
                            return True
                    
                    # while loop breaks when a char 'ch' is seen in pattern.
                    # loop over string till 'ch' is found
                    while s[i] != p[j]:
                        i += 1
                        if i==len_s: # Reached EOS but 'ch' is not found. FALSE
                            return False
                    
                    # while loop breaks when 'ch' is found in string
                    # Increment i,j and look at the next one
                    i += 1
                    j += 1
                    

                    



            
test = Solution()
p = 'aaa*'
s = 'aaa'
print(test.isMatch(s,p))
