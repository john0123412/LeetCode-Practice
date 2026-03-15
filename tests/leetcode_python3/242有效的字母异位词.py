# 暴力计算

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        t_list = list(t)
        for char in s:
            if char in t_list:
                t_list.remove(char)
            else:
                return False
        return True
    

#  哈希表

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record = [0 for _ in range(26)]
        for char in s:
            record[ord(char) - ord('a')] += 1
        for char in t:
            record[ord(char) - ord('a')] -= 1
        for count in record:
            if count != 0:
                return False
        return True
# 答案————卡尔    
# Python写法一(和我一样)：
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        record = [0] * 26
        for i in s:
            #并不需要记住字符a的ASCII，只要求出一个相对数值就可以了
            record[ord(i) - ord("a")] += 1
        for i in t:
            record[ord(i) - ord("a")] -= 1
        for i in range(26):
            if record[i] != 0:
                #record数组如果有的元素不为零0，说明字符串s和t 一定是谁多了字符或者谁少了字符。
                return False
        return True
# Python写法二（没有使用数组作为哈希表，只是介绍defaultdict这样一种解题思路）：

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        for x in s:
            s_dict[x] += 1
        
        for x in t:
            t_dict[x] += 1
        return s_dict == t_dict
# Python写法三(没有使用数组作为哈希表，只是介绍Counter这种更方便的解题思路)：

class Solution(object):
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter
        a_count = Counter(s)
        b_count = Counter(t)
        return a_count == b_count