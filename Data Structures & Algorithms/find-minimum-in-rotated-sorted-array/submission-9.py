class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        minimum = nums[0]

        while l < r:
            m = (l + r)//2

            if nums[m] < nums[r]: #Then left side  
                r = m
                minimum = min(minimum, nums[m])

            else: #Then right side
                l = m + 1
                minimum = min(minimum, nums[r])

        return minimum

                