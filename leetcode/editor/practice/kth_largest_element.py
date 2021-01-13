# -*- coding: utf-8 -*-
from typing import Optional
import heapq


class KthLargest:
    """
    Solution idea:
    Create a pq(堆),keep it only having the K-largest elements by poping off smallest elements.
    With only K elements,the smallest item(self.pool[0]) will always the kth largest.

    If a new value is bigger than the smallest, it should be added to your heap.
    If it's bigger than the smallest (there are already the kth largest), it will certainly be within the kth largest of the stream.
    """
    def __init__(self, k: int, nums):
        self.pool = nums
        self.k = k
        heapq.heapify(self.pool)
        while len(self.pool) > k:
            heapq.heappop(self.pool)

    def add(self, val: int) -> int:
        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]


class Solution:
    """
    Find K-largest element in an array
    """
    def findKthLargest(self, nums: [int], k):
        """
        Use the direct way
        :param nums: array
        :return: K-th largest element of the array
        """
        nums.sort()
        return nums[-k]

    def findKthLargest1(self, nums: [int], k: int) -> int:
        """
        Quick sort
        """
        pivot = nums[len(nums)//2]
        left = [l for l in nums if l < pivot]
        equal = [e for e in nums if e == pivot]
        right = [r for r in nums if r > pivot]
        if k <= len(right):
            return self.findKthLargest1(right, k)
        elif (k - len(right)) <= len(equal):
            return equal[0]
        else:
            return self.findKthLargest1(left, k - len(right) - len(equal))

    def findKthLargest2(self, nums, k):
        """
        Use Max Heap
        """
        nums = [-num for num in nums]
        heapq.heapify(nums)
        res = float('inf')
        for _ in range(k):
            res = heapq.heappop(nums)
        return -res

    def findKthLargest3(self, nums, k):
        """
        Use Min Heap
        """
        min_heap = nums[:k]
        heapq.heapify(min_heap)
        for i in range(k, len(nums)):
            if nums[i] > min_heap[0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, nums[i])
        return min_heap[0]


if __name__ == '__main__':
    obj = KthLargest(3, [4, 5, 8, 2])
    param_1 = obj.add(4)
    print(param_1)
    param_2 = obj.add(5)
    print(param_2)
    param_3 = obj.add(8)
    print(param_3)
    param_4 = obj.add(9)
    print(param_4)
    param_5 = obj.add(9)
    print(param_5)
    param_6 = obj.add(10)
    print(param_6)



