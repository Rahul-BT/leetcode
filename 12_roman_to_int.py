class Solution(object):
    def factor(self, val, base,pw):
        val = val-base
        fact = [base]
        while val:
            val = val-pw
            fact.insert(0,pw)

        return fact

    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        base = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}
        key = [1,5,10,50,100,500,1000] 
        pw=0
        roman=''
        pref=''
        

        while num:

            if num%10 != 0:
                v = num%10 # 600%10=0
                v = v * (10**pw) # 0x10=0
            else:
                pw +=1
                num = num//10
                continue
            
            while v > 1999:
                v = v-1000
                pref = pref+ base[1000]
                
            
            for i in key:
                if v == i:
                    roman = base[i] + roman
                    break
                
                elif v == 4*(10**pw): # if v==40
                    temp = v+10**pw
                    roman = base[key[key.index(temp)-1]] + base[temp] + roman #  X + L + roman
                    break

                elif v == 9*(10**pw): # if v==90
                    temp = v+10**pw
                    roman = base[key[key.index(temp)-2]] + base[temp] + roman #  X + L + roman
                    break


                elif v < i: # 80 <100 -> True
                    l_ = self.factor(v, key[key.index(i)-1], 10**pw) # return [50, 10, 10]
                    for j in l_:
                        roman = base[j] + roman
                    break

            num = num//10
            pw += 1

            
        return pref+roman if pref else roman
    
    # Easier Method
    def intToRoman1(self, num):
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        res, i = "", 0
        while num:
            res += (num//values[i]) * numerals[i]
            num %= values[i]
            i += 1
        return res
        


        
test = Solution()
num = 3999

print(test.intToRoman1(num))