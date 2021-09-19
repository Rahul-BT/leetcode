class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Check if x lies between -2**31 and 2**31-1
        if (x > 2**31 - 1) and (x < -2**31):
            return False
        # If x is negative return False
        if x<0:
            return False
        # If x is a digit, return True
        elif x<10:
            return True
        
        #Reverse the number and check
        temp = x
        rev = 0
        while temp:
            rev = rev*10 + temp%10
            temp = temp//10
        
        if rev == x:
            return True
        
        return False


        
test = Solution()
print(test.isPalindrome(x=10))