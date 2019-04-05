# -*- coding: utf-8 -*-

"""
思想其实就很像那个汉诺塔游戏，两个柱子，实现在一个柱子底部持续加入大的盘子的思想
1.将所有盘子倒放到另一个柱子，加入新来的大盘子
2.再将所有的盘子顺序放入原来的柱子，这样就实现了在原来的柱子最下边（尾部）加入大盘子
python 实现算法：
Implement the following operations of a queue using stacks.
push(x) -- Push element x to the back of queue.
pop() -- Removes the element from in front of queue.
peek() -- Get the front element.
empty() -- Return whether the queue is empty.
堆栈a和b，a用作入队，b出队
（1）判队满：如果a满且b不为空，则队满
（2）判队空：如果a和b都为空，则队空
（3）入队：首先判队满。
    若队不满：（1）栈a若不满，则直接压入栈a
                        (2)若a满，则将a中的所有元素弹出到栈b中，然后再将元素入栈a **其实python中的list不存在满的情况**
（4）出队：(1)若b空就将a中的所有元素弹出到栈b中，然后出栈
                      （2）b不空就直接从b中弹出元素
"""


class MyQueue(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.stack1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.empty():
            return None
        if self.stack2:
            return self.stack2.pop()
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if self.empty():
            return None
        if self.stack2:
            return self.stack2[-1]
        else:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
            return self.stack2[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.stack1 == [] and self.stack2 == []

# Your MyQueue object will be instantiated and called as such:


if __name__ == '__main__':

    obj = MyQueue()
    obj.push(3)
    obj.push(4)

    param_2 = obj.pop()
    print(param_2)
    param_3 = obj.peek()
    print(param_3)
    param_4 = obj.empty()
    print(param_4)

