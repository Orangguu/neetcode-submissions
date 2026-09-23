class Solution:

    brackets = {
        '(' : ')',
        '[' : ']',
        '{' :'}'
    }
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p in self.brackets:
                stack.append(p)
            if p not in self.brackets:
                if len(stack) > 0:
                    if p == self.brackets[stack[-1]]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False                    
        if stack == []:
            return True
        else:
            return False



            
