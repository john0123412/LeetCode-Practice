#include <queue>
int pop() {
    int size = que1.size();
    size--;
    // 1. 将前 n-1 个元素转入 que2
    while (size--) {
        que2.push(que1.front());
        que1.pop();
    }

    // 2. 记录并弹出目标元素（栈顶）
    int result = que1.front();
    que1.pop();

    // 3. 直接交换两个队列的控制权，无需手动循环清空
    // 交换后，que1 拿回了数据，que2 变回了空队列
    std::swap(que1, que2); 

    return result;
}