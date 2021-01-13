# -*- coding: utf-8 -*-
from typing import List, Optional

"""
归并排序：分而治之的思想。
1.递归merge_sort_between函数，对数组进行分操作，并对各部分递归
2.merge函数，合函数，对分开后两部分，开辟新的内存空间进行合并
"""


def merge_sort(a):
    return _merge_sort_between(a, 0, len(a)-1)


def _merge_sort_between(a, low, high):
    if low < high:
        mid = low + (high - low)//2  # 此处因为公式写错导致出现bug，真是不认真啊
        _merge_sort_between(a, low, mid)
        _merge_sort_between(a, mid + 1, high)
        _merge(a, low, mid, high)


def _merge(a, low, mid, high):
    i, j = low, mid + 1
    tmp = []
    while i <= mid and j <= high:
        if a[i] < a[j]:
            tmp.append(a[i])
            i += 1
        else:
            tmp.append(a[j])
            j += 1

    # 确定那一部分还有剩余数据，找到起始位置和结束位置
    start = i if i <= mid else j
    end = mid if i <= mid else high
    tmp.extend(a[start: end+1])
    a[low: high + 1] = tmp


if __name__ == '__main__':
    a1 = [3, 5, 6, 7, 8]
    a2 = [2, 2, 2, 2]
    a3 = [4, 3, 2, 1]
    a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    merge_sort(a1)
    print(a1)
    merge_sort(a2)
    print(a2)
    merge_sort(a3)
    print(a3)
    merge_sort(a4)
    print(a4)


