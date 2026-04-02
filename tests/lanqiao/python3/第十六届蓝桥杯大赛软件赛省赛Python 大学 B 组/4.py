# 小蓝有一个字符串 s，他特别喜欢由以下三个字符组成的单词：l,q,b，任意顺序都可以，一共有 6 种可能：lqb, lbq, qlb, qbl, blq, bql。
# 现在他想从 s 中，尽可能切割出多个他喜欢的单词，请问最多能切割出多少个？单词指的是由若干个连续的字符组成的子字符串。


import os
import sys

# 请在此输入您的代码
def solve():
    try:
        s = sys.stdin.read().strip()
    except EOFError:
        return
    if not s or len(s) < 3:
        print(0)
        return
    cnt = 0
    i = 0
    while i < len(s) - 2:
        if sorted(s[i:i+3]) ==['b', 'l', 'q']:
            cnt += 1
            i += 3
        else:
            i += 1
    print(cnt)

if __name__ == "__main__":
    solve()

