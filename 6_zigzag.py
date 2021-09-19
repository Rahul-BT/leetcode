class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        i=0
        step = 1
        a = [""] * numRows

        if numRows == 1:
            return s

        for ch in s:

            if i == numRows-1:
                step = -1
            if i == 0:
                step = +1
            
            a[i] += ch
            i += step
        
        return ''.join(a)


test = Solution()
s = "AB"
val = test.convert(s, numRows=1)
print(val)