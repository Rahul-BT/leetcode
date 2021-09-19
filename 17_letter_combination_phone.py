class Solution(object):
    def combine(self, a, b):
        ret= []
        for i in a:
            for j in b:
                ret.append(i+j)
        return ret

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        db={
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        d1= db[digits[0]]

        for d in digits[1:]:
            d1 = self.combine(d1, db[d])
        
        return d1


test = Solution()
digits = "23"
print(test.letterCombinations(digits))