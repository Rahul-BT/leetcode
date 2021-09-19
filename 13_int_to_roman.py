class Solution(object):
    def romanToInt1(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]

        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return values[numerals.index(s)]

        elif s[0:2] in numerals:
            return values[numerals.index(s[0:2])] + (len(s[2:])>0)*self.romanToInt(s[2:])
        
        elif s[0] in numerals:
            return values[numerals.index(s[0:1])] + (len(s[1:])>0)*self.romanToInt(s[1:])


test = Solution()
s= "MCMXCIV"
print(test.romanToInt(s))