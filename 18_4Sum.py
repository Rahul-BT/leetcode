class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        ret = []

        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            t_ = target - nums[i]
            flag = 0
            for j in range(i+1, len(nums)-2):
                if j>1+i and nums[j] == nums[j-1]:
                    continue

                st= j+1
                end= len(nums)-1

                while st< end:
                    s= nums[j]+nums[st]+nums[end]
                    if s==t_:
                        ret.append([nums[i], nums[j], nums[st], nums[end]])
                        while st<end and nums[st]==nums[st+1]: st +=1
                        while st<end and nums[end]==nums[end-1]: end -=1

                        st +=1
                        end -=1
                    elif s>t_:
                        end -=1
                    else:
                        st +=1
        return ret

test = Solution()
nums= [-2,-1,0,0,1,2]
target = 0

# nums= [2,2,2,2,2]
# target= 8

# nums= [-2,-1,-1,1,1,2,2]
# target= 0

print(test.fourSum(nums, target))
