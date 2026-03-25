from typing import List
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # g是胃口值，s是饼干尺寸
        g.sort()
        s.sort()
        count = 0
        index = len(s) - 1
        for i in range(len(g)-1,-1,-1):
            if index < 0:
                break
            if g[i] <= s[index]:
                count += 1
                index -= 1
        return count



class Solution:
    def findContentChildren(self, g, s):
        g.sort()  # 将孩子的贪心因子排序
        s.sort()  # 将饼干的尺寸排序
        index = len(s) - 1  # 饼干数组的下标，从最后一个饼干开始
        result = 0  # 满足孩子的数量
        for i in range(len(g)-1, -1, -1):  # 遍历胃口，从最后一个孩子开始
            if index >= 0 and s[index] >= g[i]:  # 遍历饼干
                # index必须在前面，防止访问越界
                result += 1
                index -= 1
        return result