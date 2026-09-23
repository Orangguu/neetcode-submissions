class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left_p = 0
        right_p = len(heights)-1
        max_area = 0

        while left_p < right_p:

            new_area = (min(heights[right_p], heights[left_p])) * (right_p - left_p)

            if max_area < new_area:
                max_area = new_area

            if heights[left_p] < heights[right_p]:
                left_p += 1
            else:
                right_p -= 1
            
        return max_area

        