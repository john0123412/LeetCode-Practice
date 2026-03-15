### 以下给定程序中，函数fun的功能是:计算形参数组x中n个正整数的平均值，并将数组中小于平均值的元素移到数组的前部，大于等于平均值的元素移到数组的后部。平均值由函数形参avg获得
from typing import List

def fun(x: List[int], n: int, avg: List[float]) -> float:
    """计算数组平均值并重新排序数组
    
    Args:
        x: 整数数组
        n: 数组长度
        avg: 用于返回平均值的列表（模拟引用传递）
    
    Returns:
        数组的平均值
    """
    if n <= 0 or not x:
        raise ValueError("数组不能为空")
    
    total = sum(x[:n])
    avg[0] = total / n
    
    # 使用双指针法优化重排序，时间复杂度从O(n²)降到O(n)
    left, right = 0, n - 1
    while left < right:
        while left < n and x[left] < avg[0]:
            left += 1
        while right >= 0 and x[right] >= avg[0]:
            right -= 1
        if left < right:
            x[left], x[right] = x[right], x[left]
            left += 1
            right -= 1
    
    return avg[0]

def get_positive_integer_input(prompt: str) -> int:
    """获取正整数输入"""
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("请输入大于0的正整数！")
                continue
            return value
        except ValueError:
            print("请输入有效的整数！")

def get_array_input(size: int) -> List[int]:
    """获取数组输入"""
    while True:
        try:
            arr_str = input(f"请输入{size}个正整数，以空格分隔: ")
            arr = [int(x) for x in arr_str.split()]
            if len(arr) != size:
                print(f"请输入恰好{size}个数字！")
                continue
            if any(x <= 0 for x in arr):
                print("所有数字必须是正整数！")
                continue
            return arr
        except ValueError:
            print("请输入有效的整数！")

# 示例用法
if __name__ == "__main__":
    try:
        size = get_positive_integer_input("请输入正整数的个数: ")
        arr = get_array_input(size)
        avg = [0.0]  # 使用列表来模拟引用传递
        average = fun(arr, size, avg)
        print(f"平均值为: {average:.2f}")
        print("调整后的数组为:", ' '.join(map(str, arr)))
    except Exception as e:
        print(f"程序出错: {e}")

