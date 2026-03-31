# ### 问题描述

# 小蓝从左到右种了 n 棵小树，第 i 棵树的高度为 hi，相邻树的间隔相同。

# 小蓝想挪走一些树，使得剩下的树等间隔分布，且从左到右高度逐渐上升（相邻两棵树高度满足右边的比左边的高），小蓝想知道最多能留下多少棵树。

# ### 输入格式

# 输入的第一行包含一个正整数 n。

# 第二行包含 n* 个正整数 h1,h2,…,hn，相邻整数之间使用一个空格分隔。

# ### 输出格式

# 输出一行包含一个整数，表示最多能留下的树的数量。

import sys
import os

def solve():
    n = int(sys.stdin.readline().strip())
    h = list(map(int,sys.stdin.readline().strip().split()))
    
    if n <= 1:
        print(n)
        return
    
    max_trees = 1
    for i in range(n):
        for d in range(1,n):
            if i + d > n:
                break

            count = 1
            curr_id = i
            next_id = i + d
            while next_id < n and h[next_id] > h[curr_id]:
                count += 1
                curr_id = next_id
                next_id += d

            if count > max_trees:
                max_trees = count
    print(max_trees)


if __name__ == "__main__":
    solve()
    