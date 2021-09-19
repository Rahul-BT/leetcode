class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if not l:
            return 0
        elif nums[0] == nums[l-1]:
            return 1, nums[0:1]
        
        st = nums[0]
        flag=1
        while flag:
            l -= 1
            if nums[l] != nums[l-1]:
                nums.insert(0,nums[l])
                l+=1
            else:
                continue
            if nums[l] == st:
                flag=0
            
        
        return l, nums

        
# n = [0,0,1,1,1,2,2,3,3,4]
n = [1,1,2]
test = Solution()
k, n_ = test.removeDuplicates(n)
print(n_[:k])