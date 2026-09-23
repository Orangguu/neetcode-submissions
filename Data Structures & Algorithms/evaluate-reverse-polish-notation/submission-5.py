class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        for token in tokens:
            match token:
                case '+':
                    sum = num_stack.pop() + num_stack.pop()
                    num_stack.append(sum)
                case '-':
                    subtrahend = num_stack.pop()
                    minuend = num_stack.pop()
                    difference = minuend - subtrahend
                    num_stack.append(difference)
                case '*':
                    product = num_stack.pop() * num_stack.pop()
                    num_stack.append(product)
                case '/':
                    dividend = num_stack.pop()
                    divisor = num_stack.pop()
                    quotient = int(divisor / dividend)
                    num_stack.append(quotient)
                case _:
                    num_stack.append(int(token))
        return num_stack[-1]