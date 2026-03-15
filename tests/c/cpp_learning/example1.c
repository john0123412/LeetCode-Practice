#include <stdio.h>
#include <string.h>
#include <stdlib.h>
 
int main() {
char* s1 = "abc";
char* s2 = "abc";
int r = memcmp(s2, s1, 3); // 小于 0
printf("memcmp result: %d\n", r);
}