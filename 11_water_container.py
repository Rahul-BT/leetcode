class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) < 1:
            return 0

        # Time limit exceeded!!
        area = 0
        for i in range(len(height)):
            for j in range(i+1, len(height)):
                t_area = min(height[i], height[j]) *(j-i) 
                if t_area > area:
                    area = t_area
        
        return area

    def maxArea2(self, height):
        if len(height) <1:
            return 0
        
        st=0
        end=len(height)-1
        max_ar=0

        while st < end:
            h_st, h_end = height[st], height[end]
            ar = min(h_st, h_end) * (end-st)
            if ar > max_ar:
                max_ar = ar

            if h_st < h_end:
                st += 1
            else:
                end -= 1
        
        return max_ar



        
test = Solution()
#h = [1,8,6,2,5,4,8,3,7]
h = [1,1000,1000,6,2,5,4,8,3,7]
print(test.maxArea2(h))