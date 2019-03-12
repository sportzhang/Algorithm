# -*- coding: utf-8 -*-

"""
1.链表反转
将当前节点的next指针指向节点的前继节点。
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverse_list(self, head):
        """
        :type head:ListNode
        :rtype: ListNode
        """
        cur, pre = head, None  # cur指向的是头，pre指向的是尾也即空节点
        while cur:
            cur.next, pre, cur = pre, cur, cur.next
        return pre


def reverse_list_recursive(head, pre=None):
    """
    采用递归的方式实现
    :type head: ListNode
    :rtype: ListNode
    """
    if not head:
        return False
    _next = head.next
    head.next = pre
    return reverse_list_recursive(_next, head)


"""
2.判断链表中是否有环
"""


class Cycle(object):
    # 使用快慢指针
    def has_cycle(self, head):
        slow = fast = head
        while slow and fast and fast.next:
            if slow is fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False


"""
3.找到一个链表开始入环的地方
The cycle could be like the following graph:
[head]------>[cycle_start]------>[cycle_start]
after we applied fast/slow runner algorithm, that says fast slow runner will meet at some point,
called [MeetPoint],inside the cycle loop.
[head]------>[cycle_start]------>[MeetPoint]------>[cycle_start]
now we give the distance about x,y and z:
[head]---x--->[cycle_start]---y--->[MeetPoint](fast/slow runner)---z--->[cycle_start]
At this moment,fast and slow runner are both at [MeetPoint]
The problem equal to "how many steps slow runner run to [Cycle_start]?"
in other words,"how many steps is z distance?"

The distance run by slow runner = x+y
The distance run by fast runner = x+y+z+y
since fast runner is tow times faster than slow runner.
fast = 2*(slow)
so:
x+y+z+y=2*(x+y)
so we can get:
z=x

it means that slow runner should run z steps to [cycle_start] point from [MeetPoint]
And z distance is the same as x distance.

so the idea is that:
When slow and faster runner met,set a new runner from [head].
When slow and new runner meet again,tha is [cycle_start].
"""


class Begin(object):
    def cycle_start(self, head):
        slow = fast = head
        while slow and fast and fast.next:
            if slow is fast:
                return True
            slow = slow.next
            fast = fast.next.next
        new_slow = head
        while slow != new_slow:
            new_slow = new_slow.next
            slow = slow.next

    def cycle_start1(self, head):
        slow = fast = new_slow = head
        while slow and fast and fast.next:
            fast, slow = fast.next.next, slow.next
            if slow == fast:
                while slow != new_slow:
                    slow, new_slow = slow.next, new_slow.next
                return slow
        return None


"""
4.链表相邻元素交换位置
"""


class Swap(object):
    """
    设置一个头指针，头指针指向head节点，要交换的也即是头指针接下来的两个节点，每次交换完成，移动两个节点长度，也即是将头指针向前走两步
    """
    def swap_pairs(self, head):
        pre, pre.next = self, head
        while pre.next and pre.next.next:  # 存在待交换的两个节点则进行交换，只有一个或者不存在就不再交换
            a = pre.next  # 第一个节点
            b = a.next  # 第二个节点
            pre.next, b.next, a.next = b, a, a.next
            pre = a  # 重置头指针，实际就是指向下一组待交换的两个元素中前一个元素的前面一个指针位置
        return self.next


"""
reverse nodes in k group
    Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
    k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a
    multiple of k then left-out nodes in the end should remain as it is.
参考博客：https://blog.csdn.net/qq_17550379/article/details/80696835#comments
"""


class ReverseInGroup(object):
    def reverse_k_group(self, head, k):
        dummy = jump = ListNode(0)
        dummy.next = l = r = head
        while True:
            count = 0
            while r and count < k:
                r = r.next
                count = count + 1
            if count == k:
                cur, pre = l, r
                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur
                jump.next, jump, l = pre, l, r
            else:
                return dummy.next


if __name__ == '__main__':
    s = Solution()
    a_link = ListNode(6)
    print(a_link)



