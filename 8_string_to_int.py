class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        extract = "0"
        sign = 1
        sign_flag = 1

        for ch in s:
            if ch == '-' and sign_flag:
                sign = -1
                sign_flag=0
            elif ch == '+' and sign_flag:
                sign = +1
                sign_flag=0
            elif ch.isdigit():
                extract += ch
                sign_flag=0
            else:
                break
            
        extract = int(extract) * sign
        
        if (extract > 2**31 -1):
            return 2**31 -1
        elif (extract < -2**31):
            return -2**31
        
        return extract
        
test = Solution()
print(test.myAtoi(s="      -11919730356x"))