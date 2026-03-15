from lc_definitions import *


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        res: List[str] = []
        digit_to_char = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

        def backtracking(path: str, index: int) -> None:
            if index == len(digits):
                res.append(path)
                return

            digit = int(digits[index])
            letters = digit_to_char[digit]
            for ch in letters:
                backtracking(path + ch, index + 1)

        backtracking("", 0)
        return res

#更一般的写法
class Solution:
    def __init__(self):
        self.letterMap = [
            "",  # 0
            "",  # 1
            "abc",  # 2
            "def",  # 3
            "ghi",  # 4
            "jkl",  # 5
            "mno",  # 6
            "pqrs",  # 7
            "tuv",  # 8
            "wxyz"  # 9
        ]
        self.result = []
        self.s = ""

    def backtracking(self, digits, index):
        if index == len(digits):
            self.result.append(self.s)
            return
        digit = int(digits[index])  # 将索引处的数字转换为整数
        letters = self.letterMap[digit]  # 获取对应的字符集
        for i in range(len(letters)):
            self.s += letters[i]  # 处理字符
            self.backtracking(digits, index + 1)  # 递归调用，注意索引加1，处理下一个数字
            self.s = self.s[:-1]  # 回溯，删除最后添加的字符

    def letterCombinations(self, digits):
        if len(digits) == 0:
            return self.result
        self.backtracking(digits, 0)
        return self.result


# 回溯优化使用列表


class Solution:
    def __init__(self):
        self.letterMap = [
            "",  # 0
            "",  # 1
            "abc",  # 2
            "def",  # 3
            "ghi",  # 4
            "jkl",  # 5
            "mno",  # 6
            "pqrs",  # 7
            "tuv",  # 8
            "wxyz"  # 9
        ]

    def getCombinations(self, digits, index, path, result):
        if index == len(digits):
            result.append(''.join(path))
            return
        digit = int(digits[index])
        letters = self.letterMap[digit]
        for letter in letters:
            path.append(letter)
            self.getCombinations(digits, index + 1, path, result)
            path.pop()

    def letterCombinations(self, digits):
        result = []
        if len(digits) == 0:
            return result
        self.getCombinations(digits, 0, [], result)
        return result

