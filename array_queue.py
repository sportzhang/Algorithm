# -*- coding: utf-8 -*-
"""
用数组实现队列queue:用数组实现的队列是顺序队列，主要操作有入队和出队操作。
"""

from typing import Optional


class DynamicQueue:
    """
    算法步骤：
    1.入队列
    （1）判断尾指针大小是否位等于队列存储容量
        是
        （1.2）判断头指针是否位于队列开头，
            是，队列已满，无法插入
            否，队列未满，将队列进行前部搬移
                a.数据整段往前重新复制搬移
                b.将尾指针重新赋值，将头指针指0
        否
        （2）判断尾指针大小是否等于现有队列的长度
            是，直接在队列尾部插入数据
            否，在尾指针位置插入数据
        尾指针加1

    2.出队列
    （1）判断头指针和尾指针是否相同
        否，找到队列头并返回结果，将头指针后移进行赋值
        是，队列已经为空，无法进行删除操作

    """
    def __init__(self, capacity: int):
        self._items = []
        self._head = 0
        self._tail = 0
        self._capacity = capacity

    def enqueue(self, item: str):
        if self._tail == self._capacity:
            if self._head == 0:
                return False
            self._items[0:self._tail-self._head] = self._items[self._head:self._tail]
            self._tail -= self._head
            self._head = 0
        if self._tail == len(self._items):
            self._items.append(item)
        else:
            self._items[self._tail] = item
        self._tail += 1
        return True

    def dequeue(self) -> Optional[str]:
        if self._head != self._tail:
            temp = self._items[self._head]
            self._head += 1
            return temp

    def __repr__(self):
        return " ".join(item for item in self._items[self._head:self._tail])


if __name__ == '__main__':
    dynamic_queue = DynamicQueue(10)
    for i in range(10):
        dynamic_queue.enqueue(str(i))

    print(dynamic_queue)

    for _ in range(3):
        dynamic_queue.dequeue()

    print(dynamic_queue)

    dynamic_queue.enqueue("7")
    print(dynamic_queue)
    dynamic_queue.enqueue("8")
    print(dynamic_queue)








