

import os
import sys

# 请在此输入您的代码
def solve():
    w, h, v = map(int, sys.stdin.readline().split())
    
    for _ in range(h):
        print('Q' * w)
    for _ in range(w):
        print('Q' * (v + w))
    
if __name__ == "__main__":
    solve()