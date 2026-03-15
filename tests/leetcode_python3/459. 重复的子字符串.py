#暴力解法
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        if n <= 1:
            return False
        substr = ""
        for i in range(1,n//2+1):
            if n%i == 0:
                substr = s[:i]
                if substr * (n//i) == s:
                    return True
        return False

#移动匹配
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        if n <= 1:
            return False
        ss = s[1:]+s[:-1]
        return s in ss

#KMP
class Solution:
    def getNext(s:str,next:list):
        j = 0
        for i in range(1,len(s)):
            while j > 0 and s[i] != s[j]:
                j = next[j-1]
            if s[i] == s[j]:
                j += 1
            next[i] = j
        
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        if n <= 1:
            return False
        next = [0]*n
        Solution.getNext(s,next)
        if next[-1] != 0 and n%(n - next[-1]) == 0:
            return True
        return False

#（版本一） 前缀表 减一

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:  
        if len(s) == 0:
            return False
        nxt = [0] * len(s)
        self.getNext(nxt, s)
        if nxt[-1] != -1 and len(s) % (len(s) - (nxt[-1] + 1)) == 0:
            return True
        return False
    
    def getNext(self, nxt, s):
        nxt[0] = -1
        j = -1
        for i in range(1, len(s)):
            while j >= 0 and s[i] != s[j+1]:
                j = nxt[j]
            if s[i] == s[j+1]:
                j += 1
            nxt[i] = j
        return nxt
#（版本二） 前缀表 不减一

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:  
        if len(s) == 0:
            return False
        nxt = [0] * len(s)
        self.getNext(nxt, s)
        if nxt[-1] != 0 and len(s) % (len(s) - nxt[-1]) == 0:
            return True
        return False
    
    def getNext(self, nxt, s):
        nxt[0] = 0
        j = 0
        for i in range(1, len(s)):
            while j > 0 and s[i] != s[j]:
                j = nxt[j - 1]
            if s[i] == s[j]:
                j += 1
            nxt[i] = j
        return nxt