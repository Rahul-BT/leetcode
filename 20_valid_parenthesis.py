class Solution(object):
    def isValid1(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        f1=[0,0,0]

        e1 = "([{"
        e2 = ")]}"
        i=0
        chk= []
        while i<len(s):
            if s[i] in e1:
                v_ = e1.index(s[i])
                chk.append(v_)
                f1[v_] += 1 
            elif s[i] in e2:
                b_ = e2.index(s[i])
                if b_ not in chk[-1:]:
                    return False
                f1[b_] -= 1
                chk.pop()
            i+=1

            if -1 in f1:
                return False

        if sum(f1) == 0:
            return True
        else:
            return False
    
    def isValid(self, s):
        ck = ""
        i=0
        flag=0
        if len(s)%2==1:
            return False
        while i< len(s):
            if s[i] in "([{":
                flag = 1
            if s[i] == '(':
                ck += 'a'
            elif s[i] == '[':
                ck += 'b'
            elif s[i] == '{':
                ck += 'c'

            if s[i] == ')' and ck[-1:]=='a':
                ck = ck[:-1]
            elif s[i] == ']' and ck[-1:]=='b':
                ck = ck[:-1]
            elif s[i] == '}' and ck[-1:]=='c':
                ck = ck[:-1]
            elif s[i] in ")]}":
                return False
            i += 1
        
        if ck == "" and flag:
            return True
        else:
            return False
    def fasterStack(self,s):
        # Using stack to check, similar to the first function but BETTER!
        d = {'(':')', '{':'}','[':']'}
        stack = []
        for i in s:
            if i in d:  
                stack.append(i)
            elif len(stack) == 0 or d[stack.pop()] != i:
                return False
        return len(stack) == 0




        
test = Solution()
s ="()))"

print(test.isValid(s))