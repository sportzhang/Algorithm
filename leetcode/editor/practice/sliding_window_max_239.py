# -*- coding: utf-8 -*-
"""
leetcode 235:
Given an array nums, there is a sliding window of size k which is moving from the very left of
the array to the very right. You can only see the k numbers in the window. Each time the sliding
window moves right by one position. Return the max sliding window.
用数组来实现window和结果res，其实window是一个deque(双端队列)，记录的是元素的下标
"""


def maxSlidingWindow(nums, k):
    if nums is None:
        return []
    window, res = [], []
    for i, v in enumerate(nums):
        if i >= k and window[0] <= i - k:
            window.pop(0)  # 从头部删除一个元素，实现的是窗口的滑动
        while window and nums[window[-1]] <= v:
            window.pop()  # 实现的是保留窗口中的最大元素，并且最大元素最后将位于双端队列的头部，即最左侧
        window.append(i)  # 窗口滑动，进入新的元素
        if i >= k-1:  # 已经满足窗口长度要求，所以可以将窗口中的最大元素输出了
            res.append(nums[window[0]])
    return res


if __name__ == '__main__':
    a = [1, 5, 7, 2, 0, -1, 3]
    print(maxSlidingWindow(a, 3))








