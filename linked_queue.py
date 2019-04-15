# -*- coding: utf-8 -*-
from typing import Optional


class Node:
    def __init__(self, data: str, next=None):
        self.data = data
        self._next = next


class LinkedQueue:
    def __init__(self):
        self._head: Optional(str) = None
        self._tail: Optional(str) = None

    def enqueue(self, value):
        new_node = Node(value)
        if self._tail:
            self._tail._next = new_node
        else:
            self._head = new_node
        self._tail = new_node

    def dequeue(self) -> Optional[str]:
        if self._head:
            value = self._head.data
            self._head = self._head._next
            return value
        else:
            return None

    def __repr__(self):
        values = []
        current = self._head
        while current:
            values.append(current.data)
            current = current._next
        return "->".join(item for item in values)


if __name__ == "__main__":
    q = LinkedQueue()
    for i in range(10):
        q.enqueue(str(i))
    print(q)

    for _ in range(3):
        q.dequeue()
    print(q)

    q.enqueue("7")
    q.enqueue("8")
    print(q)



