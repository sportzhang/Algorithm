# -*- coding: utf-8 -*-
import random
from typing import List, Optional

"""
快速排序：最简易版实现，此时并不满足稳定性的要求，也就是说，相同的元素排序前后，顺序可能会发生变化。
"""


def q_sort(a):
    if len(a) <= 1:
        return a
    pivot = a[0]
    less = [i for i in a[1:] if i <= pivot]
    more = [m for m in a[1:] if m > pivot]
    result = q_sort(less) + [pivot] + q_sort(more)
    return result
# lambda 表达式一行代码实现

q_sort_1 = lambda array: array if len(array) <= 1 else q_sort_1([t for t in array[1:] if t <=array[0]]) + [array[0]] + q_sort_1([t for t in array[1:] if t > array[0]])


"""
稳定排序实现，相同元素排序前后位置不变。
1.设定终止条件
2.获取分区点
关于分区点的获取，有以下说明：
(1)如果不考虑空间消耗，可以申请两个数组，进行大组和小组的存放，让后再将两个组的数据顺序拷贝到数组A中，此时就不再是原地排序算法了
(2)采用空间资源消耗，可以采用原地排序的算法，通过游标i将A[p,r-1]分为两部分，A[p,i-1]都是小于pivot的，称为已处理区间，
每次都从未处理区间A[i,r-1]选一个元素A[j]与pivot进行对比，如果小于pivot，就将A[j]放到已处理区间的尾部A[i]的位置。

"""


def quick_sort(a):
    _quick_sort_between(a, 0, len(a)-1)


def _quick_sort_between(a, low, high):
    if low < high:
        k = random.randint(low, high)  # 这里的k是将pivot取值随机取值
        a[low], a[k] = a[k], a[low]

        q = partition(a, low, high)
        _quick_sort_between(a, low, q-1)
        _quick_sort_between(a, q+1, high)


def partition(a, low, high):
    pivot = a[low]
    i = low
    for j in range(low+1, high+1):
        # 对未处理区间进行遍历
        if a[j] < pivot:
            i += 1
            a[i], a[j] = a[j], a[i]  # 将小于pivot元素放到已处理区间末尾
    a[low], a[i] = a[i], a[low]  # 最后将pivot放置到中间位置，此时左边均为小，右边均为大
    return i


if __name__ == '__main__':
    a1 = [3, 5, 6, 7, 8]
    a2 = [2, 2, 2, 2]
    a3 = [4, 3, 2, 1]
    a4 = [5, -1, 9, 3, 7, 8, 3, -2, 9]
    quick_sort(a1)
    print(a1)
    quick_sort(a2)
    print(a2)
    quick_sort(a3)
    print(a3)
    quick_sort(a4)
    print(a4)





