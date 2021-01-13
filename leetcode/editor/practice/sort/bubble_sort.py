# -*- coding: utf-8 -*-
"""
冒泡排序：对于给定数组array,长度为n,从前往后两两之间进行比较，如果啊a[i]>a[j](i<j)，则进行元素交换，走完一趟为一次冒泡；
直到走一趟发现数组中不在存在逆序对，或者走完n趟，则冒泡排序完成。
时间复杂度：O(n^2)
"""


def bubble_sort(array):
    n = len(array)
    if n <= 1:
        return array
    for i in range(n):
        flag = False
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j+1] = array[j]
                array[j] = temp
                flag = True
        if not flag:
            return array


if __name__ == '__main__':
    a = [2, 4, 1, 7, 7, 9]
    # a = [2, 4, 1, 7, 5, 9]
    # a = [2, 4, 11, 17, 25, 29]

    a1 = bubble_sort(a)
    print(a1)


