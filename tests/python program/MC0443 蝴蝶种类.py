import sys

def solve():
    # 使用 sys.stdin.read 提升读取大数据的效率
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    n, m = int(input_data[0]), int(input_data[1])
    g = []
    idx = 2
    for i in range(n):
        g.append(input_data[idx : idx + m])
        idx += m

    # 1. 离散化映射 (Python 字典很方便)
    species_map = {}
    curr_id = 0
    
    # min_col[id] 记录该种类蝴蝶目前为止出现的最小列号 (0-indexed)
    # 初始化为一个大于 m 的数
    min_col = [] 
    
    # count[c] 记录有多少种蝴蝶的最小列号是 c
    count = [0] * m
    
    # 预先处理所有种类，或者在遍历时动态增加
    # 为了速度，我们直接在遍历时处理
    
    results = []
    
    for i in range(n):
        for j in range(m):
            val = g[i][j]
            if val not in species_map:
                species_map[val] = curr_id
                min_col.append(float('inf'))
                curr_id += 1
            
            s_id = species_map[val]
            if j < min_col[s_id]:
                # 如果这种蝴蝶之前在更靠右的列出现过，先把它从旧列计数中移除
                if min_col[s_id] != float('inf'):
                    count[min_col[s_id]] -= 1
                # 更新最小列并增加新列计数
                min_col[s_id] = j
                count[j] += 1
        
        # 计算当前行的 f(i, j)
        row_f = []
        current_sum = 0
        for c in range(m):
            current_sum += count[c]
            row_f.append(str(current_sum))
        results.append(" ".join(row_f))
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    solve()