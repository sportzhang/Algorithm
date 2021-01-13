# -*- coding: utf-8 -*-
from typing import List

"""
查找第一个值等于给定值的元素的下标
"""


def bsearch_left(nums: List, target: int):
    low, high = 0, len(nums)-1
    while low <= high:
        mid = low + (high - low)//2
        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return low if nums[low] == target else -1


"""
查找最后一个值等于给定值元素的下标
"""


def bsearch_right(nums: List, target: int):
    low, high = 0, len(nums)-1
    while low <= high:
        mid = low + (high - low)//2
        if nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    return high if nums[high] == target else -1


"""
查找第一个大于等于给定值的元素
"""


def bsearch_left_not_less(nums: List, target: int):
    low, high = 0, len(nums)-1
    while low <= high:
        mid = low + (high - low)//2
        if nums[mid] >= target:
            if mid ==0 or nums[mid-1] < target:
                return mid
            else:
                high = mid - 1
        else:
            low = mid + 1
    return -1


"""
查找最后一个小于等于给定值的元素：
先找到，然后往后看还有没有，没有，那就是最后一个，如果后边还有，那就往后走
没找到，缩小检索区间，高位往前走走。
"""


def bsearch_right_not_less(nums: List, target: int):
    low, high = 0, len(nums)-1
    while low <= high:
        mid = low + (high - low)//2
        if nums[mid] <= target:
            if mid == len(nums)-1 or nums[mid+1] > target:
                return mid
            else:
                low = mid + 1
        else:
            high = mid - 1


if __name__ == '__main__':
    a = [1,2,3,5,5,6,7,8]
    print(bsearch_right_not_less(a, 3))



