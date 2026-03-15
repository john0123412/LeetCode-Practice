from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = []
        for item in tokens:
            if item in ['+','-','*','/']:
                num2 = res.pop()
                num1 = res.pop()
                if item == '+':
                    res.append(num1 + num2)
                elif item == '-':
                    res.append(num1 - num2)
                elif item == '*':
                    res.append(num1 * num2)
                else:
                    res.append(int(num1 / num2))
            else:
                res.append(int(item))
        return res[0]


#Python3：
from operator import add, sub, mul

def div(x, y):
    # 使用整数除法的向零取整方式
    return int(x / y) if x * y > 0 else -(abs(x) // abs(y))

class Solution(object):
    op_map = {'+': add, '-': sub, '*': mul, '/': div}
    
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in {'+', '-', '*', '/'}:
                stack.append(int(token))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(self.op_map[token](op1, op2))  # 第一个出来的在运算符后面
        return stack.pop()
#另一种可行，但因为使用eval()相对较慢的方法:

class Solution(object):
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            # 判断是否为数字，因为isdigit()不识别负数，故需要排除第一位的符号
            if token.isdigit() or (len(token)>1 and token[1].isdigit()):
                stack.append(token)
            else:
                op2 = stack.pop()
                op1 = stack.pop()
		# 由题意"The division always truncates toward zero"，所以使用int()可以天然取整
                stack.append(str(int(eval(op1 + token + op2))))
        return int(stack.pop())