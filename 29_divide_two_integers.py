class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor  == -1 and dividend == -2**31:
            return 2**31-1
        
        elif divisor in [-1, 1]:
            return dividend*divisor

        i=0
        f1, f2 = 1, 1
        if dividend<0:
            dividend *= -1
            f1 = -1
        if divisor<0:
            divisor *= -1
            f2 = -1
        
        while dividend>=0:
            dividend = dividend-divisor
            i += 1

        return (i-1)*f1*f2

        

        
test = Solution()
print(test.divide(20,-2))