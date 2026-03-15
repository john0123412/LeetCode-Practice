#字符串的右旋转操作是把字符串尾部的若干个字符转移到字符串的前面。给定一个字符串 s 和一个正整数 k，请编写一个函数，将字符串中的后面 k 个字符移到字符串的前面，实现字符串的右旋转操作。 例如，对于输入字符串 "abcdefg" 和整数 2，函数应该将其转换为 "fgabcde"。
#输入描述
#输入共包含两行，第一行为一个正整数 k，代表右旋转的位数。第二行为字符串 s，代表需要旋转的字符串。
#输出描述
#输出共一行，为进行了右旋转操作后的字符串。
def right_rotate_string(s: str, k: int) -> str:
    k = k % len(s)  # 处理 k 大于字符串长度的情况
    return s[-k:] + s[:-k]
if __name__ == "__main__":
    k = int(input())
    s = input()
    print(right_rotate_string(s, k))  # Output: "fgabcde"
    

#s = s[len(s)-k:] + s[:len(s)-k]
#print(s)