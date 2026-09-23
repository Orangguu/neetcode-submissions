class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        suf = [1]
        res = []
        i = 1
        while i < len(nums):
            pre.append(pre[i-1] * nums[i-1])
            suf.append(suf[i-1] * nums[-i])
            i += 1

        j = 1
        while j <= len(nums):
            res.append(pre[j-1] * suf[-j])
            j += 1

        return res

        