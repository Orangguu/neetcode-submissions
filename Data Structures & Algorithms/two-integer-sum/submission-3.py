class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        size = len(nums)
        i = 0
        while i < size:
            num = nums[i]
            difference = target - num 
            if difference in seen:
                if seen[difference] < i:
                    return [seen[difference], i]
                else:
                    return [i, seen[difference]]
            seen[num] = i
            
            i += 1
                

        