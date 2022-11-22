from ast import List


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for o in operations:
            if o == 'C':
                stack.pop()
            elif o == 'D':
                stack.append(2 * stack[-1])
            elif o == '+':
                num1 = stack.pop()
                num2 = stack.pop()
                stack.append(num2)
                stack.append(num1)
                stack.append(num1 + num2)
            else:
                stack.append(int(o))
        res = 0
        while stack:
            res += stack.pop()
        return res
