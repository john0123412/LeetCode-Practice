

import os
import sys


def solve():
    try:
        data = sys.stdin.read().strip()
    except EOFError:
        return
    
    if not data:
        return 
    words = sorted(list(set(data)), key=lambda x: (len(x), x))
    best_words = ""
    beautiful_sets = {}

    for word in words:
        n = len(word)
        is_beautiful = False
        if n == 1:
            is_beautiful = True
        else:
            prefix_sorted = tuple(sorted(word[:-1]))
            if (n-1) in beautiful_sets and prefix_sorted in beautiful_sets[n-1]:
                is_beautiful = True
        if is_beautiful:
            if n not in beautiful_sets:
                beautiful_sets[n] = set()
            beautiful_sets[n].add(tuple(sorted(word)))
            if n > len(best_words):
                best_words = word
            elif n == len(best_words) :
                best_words = min(best_words, word)
    
    if best_words:
        print(best_words)

if __name__ == "__main__":
    solve()


import sys

def solve():
    # --- 1. 读取数据 ---
    # 建议：如果是在实验平台，通常 words.txt 就在当前目录
    try:
        with open('words.txt', 'r', encoding='utf-8') as f:
            data = f.read().split()
    except FileNotFoundError:
        # 如果本地没有，再尝试从标准输入读取（某些平台重定向了输入）
        data = sys.stdin.read().split()

    if not data:
        return

    # --- 2. 预处理 ---
    # 去重，并按 长度(升序) + 字典序(升序) 排序
    all_words = sorted(list(set(data)), key=lambda x: (len(x), x))
    
    # beautiful_sets 字典：键是长度，值是该长度下所有优美字符串的“排序元组指纹”
    beautiful_sets = {} 
    best_word = ""

    # --- 3. 核心逻辑 ---
    for word in all_words:
        n = len(word)
        is_beautiful = False
        
        if n == 1:
            # 长度为 1 总是优美的
            is_beautiful = True
        else:
            # 检查前 n-1 个字母排序后的“指纹”是否在上一级的优美集合中
            prefix_sorted = tuple(sorted(word[:-1]))
            if (n - 1) in beautiful_sets and prefix_sorted in beautiful_sets[n - 1]:
                is_beautiful = True
        
        if is_beautiful:
            # 将当前单词的“指纹”存入对应的长度集合中
            if n not in beautiful_sets:
                beautiful_sets[n] = set()
            beautiful_sets[n].add(tuple(sorted(word)))
            
            # 更新结果：长度优先，字典序次之
            # 因为 all_words 已经按字典序排过，同长度下第一个进来的就是字典序最小的
            if n > len(best_word):
                best_word = word
            elif n == len(best_word):
                if word < best_word:
                    best_word = word

    # --- 4. 输出 ---
    if best_word:
        print(best_word)

if __name__ == "__main__":
    solve()