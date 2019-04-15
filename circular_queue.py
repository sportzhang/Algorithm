# -*- coding: utf-8 -*-
from typing import Optional
from itertools import chain


class CircularQueue:
    """
    判断队列空和满的条件：head==tail(队列空)；(head+1)%n=head(队列满)
    """

    def __init__(self, capacity: int):
        self._items = []
        self._head = 0
        self._tail = 0
        self._capacity = capacity

    def enqueue(self, item: str):
        if (self._head + 1) % self._capacity == self._head:
            return False
        else:
            self._items.append(item)
            self._tail += (self._tail + 1) % self._capacity
            return True

    def dequeue(self):
        if self._head is self._tail:
            return None
        else:
            ret = self._items[self._head]
            self._head = (self._head + 1) % self._capacity
            return ret

    def __repr__(self) -> str:
        if self._tail >= self._head:
            return " ".join(item for item in self._items[self._head:self._tail])
        else:
            return " ".join(item for item in chain(self._items[self._head:], self._items[:self._tail]))


if __name__ == '__main__':
    q = CircularQueue(5)
    for i in range(5):
        q.enqueue(str(i))
    print(q)
    q.dequeue()
    q.dequeue()
    q.enqueue(str(5))
    print(q)

