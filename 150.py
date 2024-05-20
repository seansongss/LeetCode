from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        arithmetic = ["+", "-", "/", "*"]
        for i in tokens:
            if i not in arithmetic:
                stack.append(int(i))
            else:
                result = 0
                num1 = stack.pop()
                num2 = stack.pop()
                if i=='+':
                    result+=num1+num2
                elif i=='*':
                    result+=num1*num2
                elif i=='-':
                    result+=num2-num1
                elif i=='/':
                    if num1*num2 >= 0:
                        result+=num2//num1
                    else:
                        result+=-1*(abs(num2)//abs(num1))
                stack.append(result)
        return stack[-1]