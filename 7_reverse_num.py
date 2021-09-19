class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x//10 == 0:
            return x
        
        sign = 1
        if x<0:
            x = abs(x)
            sign = -1

        rev = 0
        while x:
            
            rev = rev*(10) + x%10
            x = x//10

            if rev > 2**31 -1:
                return 0
            elif rev < -2**31:
                return 0
        
        return rev*sign




        
test = Solution()
val = test.reverse(x=123)
print(val)