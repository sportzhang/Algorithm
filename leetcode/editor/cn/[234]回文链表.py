# 请判断一个链表是否为回文链表。 
# 
#  示例 1: 
# 
#  输入: 1->2
# 输出: false 
# 
#  示例 2: 
# 
#  输入: 1->2->2->1
# 输出: true
#  
# 
#  进阶： 
# 你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？ 
#  Related Topics 链表 双指针


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        设置快慢指针
        每次快指针增加两个，慢指针增加一个
        这样当快指针结尾时，慢指针指向了链表的中间
        用慢指针逆序链表的后半部分，利用Python交换的特性，不需要额外的tmp结点
        一个从头开始，一个从中间开始，判断两者是否相同

        参考
        作者：qsctech-sange
        链接：https://leetcode-cn.com/problems/palindrome-linked-list/solution/xing-shu-ji-jian-kuai-man-zhi-zhen-fan-zhuan-lian-/

        :type head: ListNode
        :rtype: bool
        """
        # 寻找中点
        slow, fast, prev = head, head, None
        while fast is not None:
            slow = slow.next
            fast = fast.next.next if fast.next is not None else fast.next

        # 链表反转部分,注意这里就是对链表的后半部分进行翻转，
        while slow is not None:
            '''
            上面完成快慢指针的移动后，prev=None,此时令slow.next=prev,就相当于后半部分链表的第一个节点指向None，
            slow变成slow.next，就是后半部分第二个节点，prev=slow,
            这样，下一轮再进行赋值，slow.next=prev,第二个就反过来指向第一个节点。
            '''
            slow.next, slow, prev = prev, slow.next, slow

        # 前后两部分比较，此时的prev是后半部分翻转后的第一个节点，头结点
        while head and prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True

