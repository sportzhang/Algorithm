# -*- coding: utf-8 -*-
"""
跳表的实现
"""
import random
from typing import Optional


class ListNode:
    def __init__(self, data: Optional[int] = None):
        self._data = data
        self._forwards = []  # Forward pointers


class SkipList:
    _MAX_LEVEL = 16

    def __init__(self):
        self._level_count = 1
        self._head = ListNode()
        self._head._forwards = [None]*type(self)._MAX_LEVEL
        




