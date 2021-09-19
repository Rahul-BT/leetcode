class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        dev = 10**5

        for i in range(len(nums)-2):
            origin = nums[i]
            if i > 0 and nums[i] == nums[i-1]:
                continue
            st = i+1
            end = len(nums)-1

            while st < end:
                s = nums[st]+origin+nums[end]
                d_ = abs(target-s)
                if d_ == 0:
                    return s
                elif d_ < abs(dev):
                    dev = target-s
                    ret = s
                
                if nums[st] == nums[end]:
                    break
                if s > target:
                    end -=1
                else:
                    st +=1
        return ret


test = Solution()
#n= [-1,2,1,-4]
#n= [1,1,-1,-1,3]
#n= [1,1,1,0]
n= [13,2,0,-14,-20,19,8,-5,-13,-3,20,15,20,5,13,14,-17,-7,12,-6,0,20,-19,-1,-15,-2,8,-2,-9,13,0,-3,-18,-9,-9,-19,17,-14,-19,-4,-16,2,0,9,5,-7,-4,20,18,9,0,12,-1,10,-17,-11,16,-13,-14,-3,0,2,-18,2,8,20,-15,3,-13,-12,-2,-19,11,11,-10,1,1,-10,-2,12,0,17,-19,-7,8,-19,-17,5,-5,-10,8,0,-12,4,19,2,0,12,14,-9,15,7,0,-16,-5,16,-12,0,2,-16,14,18,12,13,5,0,5,6]
t= -59
print(test.threeSumClosest(n, t))