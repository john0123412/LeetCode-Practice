#暴力算法
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for i in range(len(magazine)):
            for j in range(len(ransomNote)):
                if magazine[i] == ransomNote[j]:
                    ransomNote = ransomNote.replace(ransomNote[j], '', 1)
                    break
        if ransomNote == '':
            return True
        else:
            return False
        
# 使用字典
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        record = dict()
        for char in magazine:
            record[char] = record.get(char,0) + 1
        for char in ransomNote:
            if char not in record or record[char] == 0:
                return False
            record[char] -= 1
        return True
    

#使用数组
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        record = [0] * 26
        for char in magazine:
            record[ord(char) - ord('a')] += 1
        for char in ransomNote:
            index = ord(char) - ord('a')
            if record[index] == 0:
                return False
            record[index] -= 1
        return True
    
#（版本四）使用Counter

from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return not Counter(ransomNote) - Counter(magazine)
#（版本五）使用count

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return all(ransomNote.count(c) <= magazine.count(c) for c in set(ransomNote))
#(版本六）使用count(简单易懂)

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for char in ransomNote:
            if char in magazine and ransomNote.count(char) <= magazine.count(char):
                continue
            else:
                return False
        return True