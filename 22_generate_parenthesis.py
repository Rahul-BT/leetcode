class Solution(object):
    def generatePattern(self, n):
        st = int("10"*n, 2)
        end = int("1"*n +"0"*n, 2)
        print("Start: {}\nEnd: {}".format(st,end))

        t_ = []
        # d_ = [] 
        while (st< end+1):
            t1 = bin(st).replace("0b","")
            if t1.count("1") == t1.count("0"):
                c2=0
                fl=1
                for i in t1:
                    if i == "1":
                        c2 +=1
                    else: 
                        c2 -=1
                    if c2<0:
                        fl=0
                        break
                if fl:
                    t_.append(t1)
                    # d_.append(int(t1,2))
            st +=2
        
        #print("Accepted nos: {}\nLength: {}".format(t_, len(t_)))
        #print(d_)
        return t_
            
        
    
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        patt = self.generatePattern(n)

        temp = [p.replace("1","(").replace("0", ")") for p in patt]
        return temp
    
    def answer(self, n): #BETTER
        def dfs(results, acc, no_open, no_close):
			# success case is if both open and close are 0 AT THE SAME TIME
            if no_open == 0 and no_close == 0:
                results.append(acc)
                return
			# if either are lesser than 0, it's malformed, since we want them to be in equilibrium
            if no_close < 0 or no_open < 0:
                return
			# if no_open == no_close, we need to open before we can start closing
            if no_open == no_close:
                dfs(results, acc + '(', no_open - 1, no_close)
			# otherwise, we can just open or close, so try both possibilities!
            else:
                dfs(results, acc + ')', no_open, no_close - 1)
                dfs(results, acc + '(', no_open - 1, no_close)
            
        results = []
        dfs(results, '', n, n)
        return results
        

        
test = Solution()
#test.generatePattern(n=1)
#print(test.generateParenthesis(n=3))
print(test.answer(n=4))