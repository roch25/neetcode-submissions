class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            stack = []

        for tok in tokens:
            if tok not in ('+', '-', '*', '/'):
                stack.append(int(tok))
                continue

            op2 = stack.pop()
            op1 = stack.pop()

            if tok == '+':
                stack.append(op1 + op2)
            elif tok == '-':
                stack.append(op1 - op2)
            elif tok == '*':
                stack.append(op1 * op2)
            else:
                stack.append(int(op1 / op2))

        return stack[-1]