# 在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。 
# 
#  示例 1: 
# 
#  输入: [3,2,1,5,6,4] 和 k = 2
# 输出: 5
#  
# 
#  示例 2: 
# 
#  输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
# 输出: 4 
# 
#  说明: 
# 
#  你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。 
#  Related Topics 堆 分治算法
import random


# leetcode submit region begin(Prohibit modification and deletion)
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        def partition(left, right, pivot_index):
            # 1. move pivot to end
            pivot = nums[pivot_index]
            nums[pivot_index], nums[right] = nums[right], nums[pivot_index]

            # 2. move all smaller elements to the left
            store_id = left
            for i in range(left, right):
                if nums[i] < pivot:
                    tmp = nums[i]
                    nums[i] = nums[store_id]
                    nums[store_id] = tmp
                    store_id += 1
            # 3. move pivot to its final place
            nums[store_id], nums[right] = nums[right], nums[store_id]
            return store_id

        def select(left, right, kth_smallest):
            # Returns the k-th smallest element of list within left..right.
            # If the list contains only one element,return that element
            if left == right:
                return nums[left]

            # 先随机选定一个pivot的元素位置
            # select a random pivot_index between
            pivot_index = random.randint(left, right)
            # 根据随机选定的位置进行数组元素的大小拆分： smaller pivot bigger
            pivot_index = partition(left, right, pivot_index)

            # the pivot is in its final sorted position
            if kth_smallest == pivot_index:
                return nums[kth_smallest]
            # go left
            elif kth_smallest < pivot_index:
                return select(left, pivot_index - 1, kth_smallest)
            # go right
            else:
                return select(pivot_index + 1, right, kth_smallest)

        # kth largest is (n - k)th smallest
        return select(0, len(nums) - 1, len(nums) - k)
    # leetcode submit region end(Prohibit modification and deletion)
