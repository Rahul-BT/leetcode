class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums)<3:
            return []

        nums.sort()
        ret = []
        
        for i in range(len(nums)-2):
            origin = nums[i]
            if i > 0 and nums[i] == nums[i-1]:
                continue
            st = i+1
            end = len(nums)-1

            while st < end:
                s = nums[st]+origin+nums[end]
                if s== 0:
                    exp = [origin,nums[st],nums[end]]
                    
                    # If there are repeating values, skip them
                    while st < end and nums[st] == nums[st+1]:
                        st +=1
                    while st < end and nums[end-1] == nums[end]:
                        end -=1
                    
                    st +=1
                    end -=1
                    
                    # The below exp increases the runtime 1600ms !!
                    #if exp not in ret:
                    #    ret.append(exp)

                    ret.append(exp)


                elif s > 0:
                    end -=1
                else:
                    st +=1
        return ret
    

            

test = Solution()
#n= [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
n= [0,0,0]
print(test.threeSum(n))