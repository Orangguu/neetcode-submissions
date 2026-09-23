class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first_set = {}
        for x in s:
            if x in first_set:
                first_set[x] += 1
            else:
                first_set[x] = 1
        for x in t:
            if x in first_set:
                first_set[x] -= 1
            else:    
                return False
        for x in first_set:
            if first_set[x] != 0:
                return False
        return True


            

        