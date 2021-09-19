# Palindrome in substring

class Solution:
    """
    Time Complexity is O(n^2)
    YouTube expln: https://www.youtube.com/watch?v=y2BD4MJqV20&t=8s&ab_channel=NickWhite
    """

    def checkPalin(self, s, left, right):
        
        while (left >=0 and right <len(s) and s[left]==s[right]):
            left -= 1
            right += 1
        return right - left - 1

    def longestPalindrome(self,s):
        # start and end represents the end-points of 
        # the palindrome substring
        start = 0
        end = 0
        
        for i in range(len(s)):
            len1 = self.checkPalin(s, i, i)
            len2 = self.checkPalin(s, i, i+1)
            L = max(len1, len2)
            if L> (end-start+1):
                start = i - (L-1)//2
                end = i + L//2
        
        return s[start:end+1]

test = Solution()
s = "zaacbcahg"
val = test.longestPalindrome(s)
print(val)
