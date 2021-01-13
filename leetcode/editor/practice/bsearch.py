# -*- coding: utf-8 -*-
from typing import List


def bsearch(nums: List, target: int) -> int:
    """
    :param nums: 待查找数列
    :param target: 查找目标
    :return: 查找结果
    """
    low, high = 0, len(nums) - 1
    while low <= high:
        mid = low + (high - low)//2
        if nums[mid] == target:
            return nums[mid]
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == '__main__':
    a = [1, 2, 3, 7, 10, 23]
    print(bsearch(a, 7))

