#include <stdio.h>
#include <string.h>
void getNext(int* next, const char* s) {
    int j = 0;        // j 代表：前缀的末尾位置，也代表了当前最长相等前后缀的长度
    next[0] = 0;      // 只有一个字符时，没有前后缀，长度为 0

    // i 代表：后缀的末尾位置
    for (int i = 1; s[i] != '\0'; i++) {
        
        // 【情况 1】前后缀不匹配了
        // 这是一行最烧脑的代码：回溯。
        // 既然当前位置不匹配，我们就看前一个位置能跳到哪里，直到找着匹配的或者退回起点
        while (j > 0 && s[i] != s[j]) {
            j = next[j - 1]; 
        }

        // 【情况 2】前后缀匹配成功
        if (s[i] == s[j]) {
            j++; // 长度加 1
        }

        // 把计算出来的长度赋给 next 数组
        next[i] = j;
    }
}
int strStr(char* haystack, char* needle) {
    int h_len = strlen(haystack);
    int n_len = strlen(needle);
    if (n_len == 0){
        return 0;
    }
    int next[n_len];
    getNext(next, needle);
    int j = 0; // j 代表当前匹配到的 needle 的位置
    for (int i = 0; i < h_len; i++){
        while (j > 0 && haystack[i] != needle[j]){
            j = next[j - 1];
        }
        if (haystack[i] == needle[j]){
            j++;
        }
        if (j == n_len){
            return i-n_len + 1;
        }
    }
    return -1;
}