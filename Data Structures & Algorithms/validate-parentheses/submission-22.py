class Solution:

    brackets = {
        ')' : '(',
        ']' : '[',
        '}' :'{'
    }
    def isValid(self, s: str) -> bool:
        stack = []
        for p in s:
            if p in self.brackets:
                if stack and stack[-1] == self.brackets[p]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(p)

        return stack == []



            
