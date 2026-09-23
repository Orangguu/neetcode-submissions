class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        minimum = nums[0]

        while l < r:
            m = (l + r)//2

            if nums[l] < nums[r]:

                if nums[l] < nums[m]:
                    minimum = min(minimum, nums[l])
                    r = m
                else:
                    minimum = min(minimum, nums[m])
                    l = m + 1
            else:
                if nums[r] < nums[m]:
                    minimum = min(minimum, nums[r])
                    l = m + 1
                else:
                    minimum = min(minimum, nums[m])
                    r = m

        return minimum

                