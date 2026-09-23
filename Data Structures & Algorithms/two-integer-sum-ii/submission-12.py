class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l_ptr = 0
        r_ptr = len(numbers)-1
        current_sum = numbers[r_ptr] + numbers[l_ptr]
        while current_sum != target:
            if current_sum > target:
                r_ptr -= 1
            elif current_sum < target:
                l_ptr += 1
            current_sum = numbers[r_ptr] + numbers[l_ptr]
        if current_sum == target:
            return [l_ptr+1, r_ptr+1]
        
            