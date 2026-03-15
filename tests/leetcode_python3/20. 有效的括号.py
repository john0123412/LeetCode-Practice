class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        stack = []
        for item in s:
            if item in ['(', '[', '{']:
                stack.append(item)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if item == ')' and top != '(':
                    return False
                elif item == ']' and top != '[':
                    return False
                elif item == '}' and top != '{':
                    return False
        return not stack
    
# 方法一，仅使用栈，更省空间
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        for item in s:
            if item == '(':
                stack.append(')')
            elif item == '[':
                stack.append(']')
            elif item == '{':
                stack.append('}')
            elif not stack or stack.pop() != item:
                return False
        return not stack
    
# 方法二，使用字典
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        for item in s:
            if item in mapping.keys():
                stack.append(mapping[item])
            elif not stack or stack[-1] != item: 
                return False
            else: 
                stack.pop()
        return True if not stack else False