class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([char for char in s if char.isalnum()]).lower()
        new_s = s[::-1]
        if s == new_s:
            return True
        else:
            return False
