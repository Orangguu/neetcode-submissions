class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([char for char in s if char.isalnum()]).lower()
        idx = 0
        print(len(s)//2)
        while idx < len(s)/2:
            if s[idx] != s[-idx-1]:
                return False
            else:
                idx += 1
        return True
