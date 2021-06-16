# -*-coding: utf-8 -*-
# Definition for singly-linked list.


class DBListNode(object):
    def __init__(self, x, y):
        self.key = x
        self.val = y
        self.prev = None
        self.next = None


class LRUCache:
    """
    实现本题的两种操作，需要用到一个哈希表和一个双向链表。在面试中，面试官一般会期望读者能够自己实现一个简单的双向链表，而不是使用语言自带的、封装好的数据结构。
    在 Python 语言中，有一种结合了哈希表与双向链表的数据结构 OrderedDict，只需要短短的几行代码就可以完成本题。在 Java 语言中，同样有类似的数据结构 LinkedHashMap。
    链接：https://leetcode-cn.com/problems/lru-cache/solution/lruhuan-cun-ji-zhi-by-leetcode-solution/

    leet code: 146
        运用你所掌握的数据结构，设计和实现一个  LRU (最近最少使用) 缓存机制。
        它应该支持以下操作： 获取数据 get 和 写入数据 put 。
        获取数据 get(key) - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。
        写入数据 put(key, value) - 如果密钥不存在，则写入其数据值。
            当缓存容量达到上限时，它应该在写入新数据之前删除最近最少使用的数据值，从而为新的数据值留出空间
    哈希表+双向链表
    哈希表: 查询 O(1)
    双向链表: 有序, 增删操作 O(1)
    Author: Ben
    """
    def __init__(self, capacity):
        self.cap = capacity
        self.hkeys = {}
        # self.top, self.tail作为哨兵节点，也就是伪头部和伪尾部
        self.top = DBListNode(None, -1)
        self.tail = DBListNode(None, -1)
        self.top.next = self.tail
        self.tail.prev = self.top

    def get(self, key):
        if key in self.hkeys.keys():
            cur = self.hkeys[key]  # 先找到节点
            # 跳出原位置
            cur.next.prev = cur.prev  # 将cur下一个节点的prev指向cur的上一个节点
            cur.prev.next = cur.next  # 将cur上一个节点的next指向cur的下一个节点
            # 最近用过的置于链表首部
            top_node = self.top.next
            self.top.next = cur
            cur.prev = self.top
            cur.next = top_node
            top_node.prev = cur

            return self.hkeys[key].val
        return -1

    def put(self, key, value):
        if key in self.hkeys.keys():
            # 先更新值，然后将最近使用过的置于链表的首部
            cur = self.hkeys[key]
            cur.val = value
            # 跳出原位置
            cur.prev.next = cur.next
            cur.next.prev = cur.prev
            # 最近用过的置于链表首部
            top_node = self.top.next
            self.top.next = cur
            cur.prev = self.top
            cur.next = top_node
            top_node.prev = cur
        else:
            # 增加新节点至首部
            cur = DBListNode(key, value)
            self.hkeys[key] = cur
            # 最近用过的置于链表首部
            top_node = self.top.next
            self.top.next = cur
            cur.prev = self.top
            cur.next = top_node
            top_node.prev = cur

            # 由于设置的capacity是2,所以这里判断是不是超过了大小，超过了就删除尾节点
            #  If the number of keys exceeds the capacity from this operation, evict the least recently used key.
            if len(self.hkeys.keys()) > self.cap:
                # 哈希链表删除对应的key
                self.hkeys.pop(self.tail.prev.key)
                # 去掉双向链表的尾节点
                self.tail.prev.prev.next = self.tail
                self.tail.prev = self.tail.prev.prev

    def __repr__(self):
        vals = []
        p = self.top.next
        while p.next:
            vals.append(str(p.val))
            p = p.next
        return '->'.join(vals)


if __name__ == '__main__':
    # Example 1:
    #
    #
    # Input
    # ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    # [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
    # Output
    # [null, null, null, 1, null, -1, null, -1, 3, 4]
    #
    # Explanation
    # LRUCache lRUCache = new LRUCache(2);
    # lRUCache.put(1, 1); // cache is {1=1}
    # lRUCache.put(2, 2); // cache is {1=1, 2=2}
    # lRUCache.get(1);    // return 1
    # lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    # lRUCache.get(2);    // returns -1 (not found)
    # lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3} ,因为此时1是最近最少使用，所以废弃了1，保留了3.
    # lRUCache.get(1);    // return -1 (not found)
    # lRUCache.get(3);    // return 3
    # lRUCache.get(4);    // return 4
    cache = LRUCache(capacity=2)
    cache.put(1, 1)
    cache.put(2, 2)
    print(cache)  # cache is {1=1, 2=2}
    print(cache.get(1))  # return 1
    cache.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    print(cache)
    print(cache.get(2))  # returns -1 (not found)
    cache.put(4, 4)
    print(cache)
    cache.get(1)
    cache.get(3)
    print(cache)
    cache.get(4)
    print(cache)

