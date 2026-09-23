class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r_ptr = 0
        l_ptr = 0
        longest_substring = 0
        len_substring = 0
        seen = set()

        while r_ptr < len(s):
            while s[r_ptr] in seen: # MOVE LEFT PTR
                seen.remove(s[l_ptr])
                len_substring -= 1
                l_ptr += 1


            seen.add(s[r_ptr])
            len_substring += 1
            r_ptr += 1
                
            if len_substring > longest_substring:
                longest_substring = len_substring
        
        return longest_substring
            