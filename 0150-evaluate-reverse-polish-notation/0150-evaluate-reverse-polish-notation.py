class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack_token = []

        for i in tokens:
            if i=="+" or i=="*" or i=="/" or i=="-":
                b = stack_token.pop()
                a = stack_token.pop()
                match i:
                    case "+":
                       c = a + b
                    case "-":
                       c = a - b
                    case "*":
                       c = a * b
                    case "/":
                       c = int(a / b)
                stack_token.append(c)
            else:
                stack_token.append(int(i))
        
        return stack_token.pop()
        