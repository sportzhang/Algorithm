# -*- coding: utf-8 -*-
from typing import List
"""
二分法的递归实现:
给定待查找数组，数组起始和结束下标，待查找对象，递归实现，所以需要给出起始下标和末尾下标。
"""


def bsearch(nums: List, target: int):
    return bsearch_recursion(nums, 0, len(nums)-1, target)


def bsearch_recursion(nums, low, high, target):
    if low > high:
        return -1
    mid = low + (high - low)//2
    if nums[mid] == target:
        return nums[mid]
    elif nums[mid] > target:
        return bsearch_recursion(nums, low, mid-1, target)
    else:
        return bsearch_recursion(nums, mid+1, high, target)


if __name__ == '__main__':
    a = [1,2,5,7,9,12,34]
    print(bsearch(a, 9))



