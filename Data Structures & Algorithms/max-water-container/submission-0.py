class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Brute
        # res = 0
        # for l in range (len(heights)):
        #     for r in range(l + 1, len(heights)):
        #         area = (r - l) * min(heights[l], heights[r])
        #         res = max(res, area)
        # return res
        res = 0
        l, r = 0, len(heights) - 1

        while l < r:
            area = (r - l) * min(heights[l], heights[r])
            res = max(res, area)
            
            if min(heights[l], heights[r]) == heights[l]:
                l += 1
            elif min(heights[l], heights[r]) == heights[r]:
                r -= 1    

        return res