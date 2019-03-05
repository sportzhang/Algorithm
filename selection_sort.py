# -*- coding: utf-8 -*-
"""
选择排序：思想类似于插入排序算法，也是讲整个数组队列分为两个部分，已排序部分和未排序部分，所谓选择也就是在未排序部分选择最小元素，
然后插入已排序部分的尾部。
"""
from typing import List


def selection_sort(l: List[int]):
    n = len(l)
    if n <= 1:
        return l
    for i in range(n):
        min_index = i
        min_val = l[i]
        for j in range(i, n):
            if l[j] < min_val:
                min_index = j
                min_val = l[j]
        l[i], l[min_index] = l[min_index], l[i]
    return l


if __name__ == '__main__':
    a = [2, 4, 7, 8, 1]
    b = selection_sort(a)
    print(b)